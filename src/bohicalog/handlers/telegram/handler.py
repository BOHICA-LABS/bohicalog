"""
This module contains the TelegramHandler class.
"""


import logging
from threading import RLock, Thread
from time import sleep

import cloudscraper  # Replaces requests and can get around cloudflare bot check
import requests
from retry import retry

from bohicalog.utils import check_key

from .buffer import Buffer
from .consts import (
    API_URL,
    FLUSH_INTERVAL,
    MAX_BUFFER_SIZE,
    MAX_MESSAGE_SIZE,
    MAX_RETRYS,
    RETRY_BACKOFF_TIME,
    RETRY_COOLDOWN_TIME,
)

__all__ = ["TelegramLoggingHandler"]

logger = logging.getLogger(__name__)


class TelegramLoggingHandler(logging.Handler):
    """
    This method is called by the logging framework to write a log message to the telegram channel.
    https://core.telegram.org/bots/api#sendmessage

    Usage:

    .. code-block:: python

        from bohicalog import logger
        from bohicalog.handlers.telegram import (
            HTMLFormatter,
            TelegramLoggingHandler,
        )

        BOT_TOKEN = TOKEN"
        CHANNEL_NAME = "chat id"  # if its public you can use the name with an @ infront: '@example'

        telegram_handler = TelegramLoggingHandler(
            BOT_TOKEN, CHANNEL_NAME, level=logging.INFO, disable_notification=False
        )

        telegram_handler.setFormatter(HTMLFormatter(use_emoji=True))

        logger.addHandler(telegram_handler)
        logger.info("Telegram test")

    """

    def __init__(
        self,
        bot_token,
        channel_name,
        level=logging.NOTSET,
        host="api.telegram.org",
        protect_content=True,
        disable_notification=False,
    ):
        """
        :param bot_token: Token of the telegram bot
        :param channel_name: channel name to write to
        :param level: Logging level
        :param host: host to use
        :param protect_content: disable forwards (default: True)
        :param disable_notification: disable notifications (default: False)
        """
        super().__init__(level)
        self.bot_token = bot_token
        self.channel_name = channel_name
        self.host = host
        self.protect_content = protect_content
        self.disable_notification = disable_notification
        self._buffer = Buffer(MAX_BUFFER_SIZE)
        self._stop_signal = RLock()
        self._writer_thread = None
        self._start_writer_thread()
        self._session = cloudscraper.create_scraper()

    @property
    def _baseurl(self):
        """
        Returns the Base url for the telegram handler.

        :rtype: str
        :return: Base url
        """
        return f"https://{self.host}/bot{self.bot_token}"

    def _get(self, resource, params=None):
        """
        Get Method for the telegram api.

        :param resource: resource to get
        :param params: params to pass
        :rtype: requests.Response
        :return: response
        """
        endpoint = f"{self._baseurl}/{resource}"

        return self._session.post(endpoint, params=params)

    @retry(
        requests.exceptions.RequestException,
        tries=MAX_RETRYS,
        delay=RETRY_COOLDOWN_TIME,
        backoff=RETRY_BACKOFF_TIME,
        logger=logger,
    )
    def write(self, message):
        """
        Write a message to the telegram channel.

        :param message:
        """

        resource = "sendMessage"
        params = {
            "chat_id": self.channel_name,
            "text": message,
            "protect_content": self.protect_content,
            "disable_notification": self.disable_notification,
        }

        # Check for parse_mode
        if getattr(self.formatter, "parse_mode", None):
            params["parse_mode"] = self.formatter.parse_mode

        response = self._get(resource, params)

        response.raise_for_status()
        if response.status_code == requests.codes.too_many_requests:
            raise requests.exceptions.RequestException("Too many requests")

    def emit(self, record: logging.LogRecord) -> None:
        """
        Emit a record.

        :param record: record to emit
        """
        message = self.format(record)
        self._buffer.write(message)

    def close(self):
        """
        Close the handler.

        """
        with self._stop_signal:
            self._writer_thread.join()

    def _write_manager(self):
        """
        Write manager.
        :return:
        """
        while True:
            # as long as we can acquire the lock, we can continue
            lock_status = self._stop_signal.acquire(blocking=False)
            if not lock_status:
                break
            else:
                self._stop_signal.release()

            sleep(FLUSH_INTERVAL)
            message = self._buffer.read(MAX_MESSAGE_SIZE)
            if message != "":
                self.write(message)

    def _start_writer_thread(self):
        """
        Start the writer thread.
        """
        self._writer_thread = Thread(target=self._write_manager)
        self._writer_thread.daemon = True
        self._writer_thread.start()

    def _get_updates(self):
        """
        Get updates from the telegram api.

        :return: updates
        """
        resource = "getUpdates"
        return self._get(resource)

    def get_chat_id(self):
        """
        Get the chat id of the channel.

        :rtype: list(int)
        :return: chat ids
        """
        response = self._get_updates()
        response.raise_for_status()
        result = []
        for update in response.json()["result"]:
            if check_key(update, "message", "chat", "id"):
                result.append(update["message"]["chat"]["id"])
            elif check_key(update, "edited_message", "chat", "id"):
                result.append(update["edited_message"]["chat"]["id"])
            elif check_key(update, "channel_post", "chat", "id"):
                result.append(update["channel_post"]["chat"]["id"])
            elif check_key(update, "edited_channel_post", "chat", "id"):
                result.append(update["edited_channel_post"]["chat"]["id"])
            elif check_key(update, "inline_query", "from", "id"):
                result.append(update["inline_query"]["from"]["id"])
            elif check_key(update, "chosen_inline_result", "from", "id"):
                result.append(update["chosen_inline_result"]["from"]["id"])
            elif check_key(update, "my_chat_member", "chat", "id"):
                result.append(update["my_chat_member"]["chat"]["id"])

        return [*set(result)]
