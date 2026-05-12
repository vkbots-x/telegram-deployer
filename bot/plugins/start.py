from pyrogram import Client, filters
from pyrogram.types import Message

from database.users import create_user
from bot.keyboards.main_keyboard import main_keyboard


@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):

    await create_user(message.from_user.id)

    text = """
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
