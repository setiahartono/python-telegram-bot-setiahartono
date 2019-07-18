def get_reply(text):
    reply = None
    replies = {
        "help": "/help: Show command list\n/sholat: Show prayer time\n/bop: Show random dog pics",
    }

    try:
        reply = replies[text.lower()]
    except KeyError:
        pass
    return reply


def text_handler(bot, update):
    print('Message from {}: "{}" (Chat ID: {})'.format(
        update.message.from_user.first_name, update.message.text,
        update.message.chat_id
    ))
    reply = get_reply(update.message.text.lower())
    if reply:
        update.message.reply_text(reply)
    else:
        update.message.reply_text("Hello, please type 'help' or /help to get command list")
