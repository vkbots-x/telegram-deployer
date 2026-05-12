import asyncio

asyncio.set_event_loop(
    asyncio.new_event_loop()
)

from pyrogram import Client

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
    plugins=dict(
        root="bot.plugins"
    )
)
