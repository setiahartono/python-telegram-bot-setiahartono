from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import commands
import message_handlers
import settings


def main():
    updater = Updater(settings.TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('bop', commands.bop))
    dp.add_handler(CommandHandler('sholat', commands.praying_time))
    dp.add_handler(CommandHandler('help', commands.help_list))

    dp.add_handler(MessageHandler(Filters.text, message_handlers.text_handler))

    print("Starting Telegram Bot: {}".format(updater.bot.name))
    updater.start_polling()
    print("Telegram Bot {} is Running".format(updater.bot.bot.username))
    updater.idle()


if __name__ == '__main__':
    main()
