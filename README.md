# Python Telegram Bot

A simple Telegram Bot made using Python.

Give the sample bot a try in Telegram app: @KadalmutanBot

### Installation

1. Clone the repository
2. Visit the Botfather via Telegram app
3. Type `/newbot` to create a Bot
4. Specify a name and username for the bot (follow BotFather instruction)
5. Get access Token, and copy it into settings.py TOKEN variable
6. Run virtual environment (`source /path/bin/activate`)
7. Install requirements (`pip install -r requirements.txt`)
8. Run application (`python main.py`)

## Deployment (Using Google Cloud Platform)
The steps below are based on a tutorial found in this article ([Building a serverless Telegram bot][tutorial])
1. Set up your Google Cloud Platform SDK and projects
2. Run `gcloud beta functions deploy webhook --runtime python37 --trigger-http`
3. If everything goes well, you will get a response like below
    ```
    availableMemoryMb: 256
    entryPoint: webhook
    httpsTrigger:
      url: [YOUR_FUNCTION_URL]
    labels:
      deployment-tool: cli-gcloud
    ```
4. Run `curl "https://api.telegram.org/bot[YOUR_BOT_TOKEN]/setWebhook?url=[YOUR_FUNCTION_URL]/webhook"` to set the webhook to handle your bot
5. Run `curl "[YOUR_FUNCTION_URL]/webhook"` to do a test run
6. Chat your bot to get response

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [tutorial]: <https://seminar.io/2018/09/03/building-serverless-telegram-bot/>