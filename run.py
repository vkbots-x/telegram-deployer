import asyncio
import threading

import uvicorn

from bot.bot import app
from utils.logger import logger

from web import app as web_app


def run_web():
    uvicorn.run(
        web_app,
        host="0.0.0.0",
        port=10000
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

    await asyncio.Event().wait()


async def main():

    thread = threading.Thread(
        target=run_web
    )

    thread.start()

    await run_bot()


if __name__ == "__main__":
    asyncio.run(main())
