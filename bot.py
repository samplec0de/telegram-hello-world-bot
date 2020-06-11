import os

from telegram import Update
from telegram.ext import Updater, MessageHandler, CallbackContext, Filters


def hello_world(update: Update, context: CallbackContext):
    update.message.reply_text('Hello, World!')


if __name__ == '__main__':
    updater: Updater = Updater(os.environ["token"], use_context=True)
    updater.dispatcher.add_handler(MessageHandler(Filters.text, hello_world))
    updater.start_polling()
    updater.idle()
