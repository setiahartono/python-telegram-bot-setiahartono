from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import commands
import message_handlers
import settings


# Get updater instance with handlers
def get_updater():
    updater = Updater(settings.TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('bop', commands.bop))
    dp.add_handler(CommandHandler('sholat', commands.praying_time))
    dp.add_handler(CommandHandler('help', commands.help_list))
    dp.add_handler(CommandHandler('location', commands.location))

    dp.add_handler(MessageHandler(Filters.text, message_handlers.text_handler))
    dp.add_handler(MessageHandler(Filters.location, message_handlers.location_handler))
    return updater


# Set a webhook for deployment
def webhook(request):
    if request.method == "POST":
        updater = get_updater()
        updater.start_polling()
        updater.idle()
    return "ok\n"


# Local function to run, for development
def main():
    updater = get_updater()

    print("Starting Telegram Bot: {}".format(updater.bot.name))
    updater.start_polling()
    print("Telegram Bot {} is Running".format(updater.bot.bot.username))
    updater.idle()


if __name__ == '__main__':
    main()
