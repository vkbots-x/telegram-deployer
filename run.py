from pyrogram import Client
from threading import Thread
import uvicorn

from web import web_app
from utils.config import (
    API_ID,
    API_HASH,
    BOT_TOKEN
)

app = Client(
    "telegram-deployer",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot.plugins")
)


def run_web():
    uvicorn.run(
        web_app,
        host="0.0.0.0",
        port=10000
    )


def main():

    Thread(target=run_web).start()

    # IMPORTANT FIX
    app.delete_webhook(
        drop_pending_updates=True
    )

    app.start()

    me = app.get_me()

    print(
        f"Bot started as @{me.username}"
    )

    app.idle()


if __name__ == "__main__":
    main()
