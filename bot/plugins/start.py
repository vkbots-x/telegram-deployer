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

    try:

        user_id = message.from_user.id

        await create_user(user_id)

        await message.reply_text(
            "Database success"
        )

    except Exception as e:

        await message.reply_text(
            f"Error:\n{e}"
        )
