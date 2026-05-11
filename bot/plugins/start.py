from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from database.users import create_user
from bot.keyboards.main_keyboard import main_keyboard


@Client.on_message(filters.command("start"))
async def start_command(
    client: Client,
    message: Message
):

    user_id = message.from_user.id

    await create_user(user_id)

    text = f"""
🚀 Welcome to Telegram Deployer

Deploy your bots directly to:

• Koyeb
• Render
• Heroku

without opening hosting dashboards.
"""

    await message.reply_text(
        text,
        reply_markup=main_keyboard()
    )
