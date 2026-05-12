import asyncio

import uvicorn

from bot.bot import app
from web import web_app

from utils.logger import logger
from utils.config import RENDER_URL


async def main():

    logger.info(
        "Starting Telegram Deployer..."
    )

    await app.start()

    webhook_url = (
        f"{RENDER_URL}/webhook"
    )

    await app.set_webhook(
        webhook_url
    )

    logger.info(
        f"Webhook set: {webhook_url}"
    )

    config = uvicorn.Config(
        web_app,
        host="0.0.0.0",
        port=10000,
        log_level="info"
    )

    server = uvicorn.Server(config)

    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
