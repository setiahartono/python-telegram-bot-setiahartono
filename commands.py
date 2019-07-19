from telegram import KeyboardButton, ReplyKeyboardMarkup

import requests
import settings
from message_handlers import get_reply


def help_list(bot, update):
    bot.send_message(update.message.chat_id, get_reply('help'))


def bop(bot, update):
    bot.send_message(update.message.chat_id, "Retrieving data....")

    print("{} requests /bop".format(update.message.from_user.first_name))
    response = requests.get('https://random.dog/woof.json')
    print("STATUS CODE {}".format(response.status_code))

    contents = response.json()
    url = contents['url']
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def location(bot, update):
    print("{} requests /location".format(update.message.from_user.first_name))
    location_keyboard = [
        [KeyboardButton(text="Share Location", request_location=True, one_time_keyboard=True)],
        [KeyboardButton(text="Cancel", one_time_keyboard=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(location_keyboard)
    bot.send_message(update.message.chat_id, "Share location?", reply_markup=reply_markup)
    print(update.message.location.latitude, update.message.location.longitude)


def praying_time(bot, update):
    bot.send_message(update.message.chat_id, "Retrieving data....")
    url = "http://muslimsalat.com/jakarta.json?key={}".format(settings.PRAYING_TIME_TOKEN)

    print("{} requests /sholat".format(update.message.from_user.first_name))
    response = requests.get(url)
    print("STATUS CODE {}".format(response.status_code))

    content = response.json()
    jadwal = content['items'][0]

    text = """
    Jadwal Sholat {} ({})\n
    Subuh: {}
    Dzuhur: {}
    Ashar: {}
    Maghrib: {}
    Isya: {}
    """.format(
        content['state'], jadwal["date_for"],
        jadwal['fajr'], jadwal['dhuhr'],
        jadwal['asr'], jadwal['maghrib'], jadwal['isha']
    )
    bot.send_message(chat_id=update.message.chat_id, text=text)
