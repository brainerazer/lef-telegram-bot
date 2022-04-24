from unittest import main
import os
import logging

from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def post(update: Update, context: CallbackContext):
    pass

def echo(update: Update, context: CallbackContext):
    print(update)
    update.message.delete()
    # context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    updater = Updater(token=os.environ['TG_TOKEN'], use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    post_handler = CommandHandler('post', post)
    echo_handler = MessageHandler((~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(post_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
