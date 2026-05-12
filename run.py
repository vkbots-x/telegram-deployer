import threading

import uvicorn

from pyrogram import idle

from bot.bot import app
from utils.logger import logger

from web import app as web_app


def run_web():

    uvicorn.run(
        web_app,
        host="0.0.0.0",
        port=10000,
        log_level="info"
    )


def main():

    logger.info(
        "Starting Telegram Deployer Bot..."
    )

    thread = threading.Thread(
        target=run_web
    )

    thread.daemon = True
    thread.start()

    app.start()

    me = app.get_me()

    logger.info(
        f"Bot started as @{me.username}"
    )

    idle()

    app.stop()


if __name__ == "__main__":
    main()
