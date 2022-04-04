import logging

import requests
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove


def echo(update, context):
    update.message.reply_text(update.message.text)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5116455777:AAGQMXmIX-Aa7CulygNaHdxAaQmZVKFQh_k'


def start(update, context):
    reply_keyboard = [['/anime_pictures', '/rock'],
                      ['/discounts', '/work_time']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        "Привет. Хорошый рок? Может аниме? Каждый найдет что-то по вкусу)",
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def help(update, context):
    update.message.reply_text(
        "Я бот справочник.")


def anime_pictures(update, context):
    update.message.reply_text(
        "Назови, кого хочешь увидеть?")


def rock(update, context):
    update.message.reply_text(
        "О, ты ценитель хорошей музыки! Чтобы избежать недопонимания, выбири степень тяжести (1-3)")


def discounts(update, context):
    update.message.reply_text(
        "Посмотри, что сейчас со скидкой: https://store.steampowered.com/specials/?l=russian")


def work_time(update, context):
    update.message.reply_text(
        "Время работы: круглосуточно.")


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("anime_pictures", anime_pictures))
    dp.add_handler(CommandHandler("rock", rock))
    dp.add_handler(CommandHandler("discounts", discounts))
    dp.add_handler(CommandHandler("work_time", work_time))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(text_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
