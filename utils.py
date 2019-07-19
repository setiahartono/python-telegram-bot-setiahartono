from telegram import ReplyKeyboardRemove


def remove_keyboard(bot, update, deletion_message):
    bot.sendMessage(update.message.chat_id, deletion_message, reply_markup=ReplyKeyboardRemove())
