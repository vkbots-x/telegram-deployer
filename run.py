import logging
from pyrogram import Client
from utils.config import API_ID, API_HASH, BOT_TOKEN

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Starting Telegram Deployer Bot...")

app = Client(
    "telegram-deployer",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot.plugins")
)

app.run()
