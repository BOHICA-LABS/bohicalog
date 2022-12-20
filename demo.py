from bohicalog import logger

logger.debug("hello")
logger.info("info")
logger.warning("warn")
logger.error("error")

# This is how you'd log an exception
try:
    raise Exception("this is a demo exception")
except Exception as e:
    logger.exception(e)

import logging

# JSON logging
import bohicalog

# Telegram logging
from bohicalog.handlers.telegram import (
    HTMLFormatter,
    MarkdownFormatter,
    TelegramFormatter,
    TelegramLoggingHandler,
)

# bohicalog.json()

# logger.info("JSON test")

# Start writing into a logfile
# bohicalog.logfile("/tmp/bohicalog-demo.log")

# Set a minimum loglevel
# bohicalog.loglevel(bohicalog.WARNING)


BOT_TOKEN = "5958012126:AAE3TzEqkdlCHgNwnkFsIohkReSfnmtLmxE"
CHANNEL_NAME = "-1001653935674"  # '@lachter_demo'

telegram_handler = TelegramLoggingHandler(
    BOT_TOKEN, CHANNEL_NAME, level=logging.INFO, disable_notification=False
)
telegram_handler.setFormatter(HTMLFormatter(use_emoji=True))

logger.addHandler(telegram_handler)
logger.info("Telegram test")
logger.warning("Telegram test")
logger.error("Telegram test")
