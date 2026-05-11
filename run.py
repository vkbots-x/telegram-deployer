import asyncio

from bot.bot import app
from utils.logger import logger


async def main():

    logger.info(
        "Starting Telegram Deployer Bot..."
    )

    await app.start()

    me = await app.get_me()

    logger.info(
        f"Bot started as @{me.username}"
    )

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
