from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import dialogflow_bot
import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('Help!')


def respond_to_an_message(bot, update):
    answer = dialogflow_bot.detect_intent_texts('my-chatty-bot', update.message.chat.id, update.message.text, 'ru')
    if answer:
        update.message.reply_text(answer)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def launch_bot(token):
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, respond_to_an_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


def main():
    load_dotenv()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    token = os.getenv('TELEGRAM_TOKEN')
    launch_bot(token)


if __name__ == '__main__':
    main()
