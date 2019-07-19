import utils

from telegram import ReplyKeyboardRemove


def get_reply(text):
    reply = None
    replies = {
        "help": "/help: Show command list\n/sholat: Show prayer time\n/bop: Show random dog pics",
        "cancel": "Command cancelled",
    }

    try:
        reply = replies[text.lower()]
    except KeyError:
        pass
    return reply


def get_callback(bot, update, text, **kwargs):
    callback_list = {
        'cancel': [utils.remove_keyboard, {'bot': bot, 'update': update, 'deletion_message': "Cancelled"}]
    }

    try:
        callback_function = callback_list[text][0]
        callback_kwargs = callback_list[text][1]
        callback_function(**callback_kwargs)
    except KeyError:
        pass


def text_handler(bot, update):
    print('Message from {}: "{}" (Chat ID: {})'.format(
        update.message.from_user.first_name, update.message.text,
        update.message.chat_id
    ))

    text = update.message.text.lower()
    reply = get_reply(text)
    get_callback(bot, update, text)

    if reply:
        update.message.reply_text(reply)
    else:
        update.message.reply_text("Hello, please type 'help' or /help to get command list")


def location_handler(bot, update):
    print('Message from {}: "{}" (Chat ID: {})'.format(
        update.message.from_user.first_name, update.message.text,
        update.message.chat_id
    ))

    bot.sendMessage(update.message.chat_id, 'Deleting keyboard', reply_markup=ReplyKeyboardRemove())
    print('Latitude: {} - Longitude: {}'.format(update.message.location.latitude, update.message.location.longitude))
