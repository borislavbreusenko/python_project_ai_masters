import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from private_consts import BOT_TOKEN


# TODO: recomendations
# TODO: link to film
# TODO: use db for user & film info


SERVER_URL = 'http://0.0.0.0:5000/'


def get_help_doc() -> str:
    help_doc = 'This bot can find info about film, use:\n/search\n'
    return help_doc


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    greeting_message = fr'Hi {user.mention_markdown_v2()}\!'
    update.message.reply_markdown_v2(greeting_message)
    help_doc = get_help_doc()
    update.message.reply_text(help_doc)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    help_doc = get_help_doc()
    update.message.reply_text(help_doc)


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def backend_touch(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    url = SERVER_URL + 'touch'
    text = requests.get(url).text
    update.message.reply_text(text)


def search(update: Update, context: CallbackContext) -> None:
    """ Return info about film: title, desription, score """
    print('New message:', update.message.text)
    film_name = ' '.join(update.message.text.split('search ')[1:])
    url = SERVER_URL + f'search/{film_name}'
    # update.message.reply_text(url)
    try:
        response = requests.get(url).json()
        update.message.reply_photo(response['poster'])
        update.message.reply_text(response['info'], parse_mode="HTML")
    except Exception:
        update.message.reply_text('Bad request!')


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("try_backend", backend_touch))
    dispatcher.add_handler(CommandHandler("search", search))

    # # on non command i.e message - echo the message on Telegram
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
