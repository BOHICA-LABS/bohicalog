import os

from dotenv import dotenv_values

import bohicalog
from bohicalog import logger

config = {
    **dotenv_values("../../../.env.shared"),  # load shared development variables
    **dotenv_values("../../../.env.secret"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}
# Telegram logging
from bohicalog.handlers.telegram import HTMLFormatter, TelegramLoggingHandler

BOT_TOKEN = config["TELEGRAM_BOT_TOKEN"]
CHANNEL_NAME = config["TELEGRAM_BOT_CHAT_ID"]

telegram_handler = TelegramLoggingHandler(
    BOT_TOKEN, CHANNEL_NAME, level=bohicalog.INFO, disable_notification=False
)
telegram_handler.setFormatter(HTMLFormatter(use_emoji=True))

logger.addHandler(telegram_handler)
logger.info("Telegram test INFO")
logger.warning("Telegram test WARN")
logger.error("Telegram test ERR")
