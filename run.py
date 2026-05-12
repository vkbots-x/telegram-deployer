import asyncio
import threading

import uvicorn

from pyrogram import idle

from bot.bot import app
from web import app as web_app

from utils.logger import logger


def run_web():

    uvicorn.run(
        web_app,
        host="0.0.0.0",
        port=10000,
        log_level="info"
    )


async def run_bot():

    logger.info(
        "Starting Telegram Deployer Bot..."
    )

    await app.start()

    me = await app.get_me()

    logger.info(
        f"Bot started as @{me.username}"
    )

    await idle()

    await app.stop()


def main():

    web_thread = threading.Thread(
        target=run_web
    )

    web_thread.daemon = True
    web_thread.start()

    asyncio.run(
        run_bot()
    )


if __name__ == "__main__":
    main()
