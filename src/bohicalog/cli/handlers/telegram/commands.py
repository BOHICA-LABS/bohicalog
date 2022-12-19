import click

__all__ = ["telegram"]


@click.group(name="telegram")
def telegram():
    """Telegram logging."""
    pass


@telegram.command(name="get_chat_id", help="Get chat id for private chat.")
@click.option("--bot-token", help="Telegram bot token.")
def get_chat_id_cmd(bot_token):
    """Get chat id for private chat."""
    from bohicalog.handlers.telegram import TelegramLoggingHandler

    handler = TelegramLoggingHandler(bot_token, None)
    click.secho(f'Chat id(s): {handler.get_chat_id()}', fg='green')


@telegram.command(name="get_updates", help="Get updates.")
@click.option("--bot-token", help="Telegram bot token.")
def get_update(bot_token):
    from bohicalog.handlers.telegram import TelegramLoggingHandler

    handler = TelegramLoggingHandler(bot_token, None)
    click.secho(handler._get_updates().text, fg='green')

