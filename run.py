import os
import threading
import logging

from fastapi import FastAPI
import uvicorn

from pyrogram import Client

from utils.config import API_ID, API_HASH, BOT_TOKEN

# ---------------- LOGGING ---------------- #

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- WEB SERVER ---------------- #

web = FastAPI()


@web.get("/")
async def root():
    return {"status": "Bot is running"}


def start_web():
    uvicorn.run(
        web,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )


# ---------------- TELEGRAM BOT ---------------- #

bot = Client(
    "telegram-deployer",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot.plugins")
)

# ---------------- MAIN ---------------- #

if __name__ == "__main__":

    print("Starting Telegram Deployer Bot...")

    # Start web server thread
    threading.Thread(target=start_web).start()

    # Start telegram bot
    bot.run()
