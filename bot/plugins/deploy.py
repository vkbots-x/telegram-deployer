import re

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, Message

from database.users import (
    update_user_state,
    get_user
)


@Client.on_callback_query(filters.regex("^deploy_bot$"))
async def deploy_button(client, callback_query: CallbackQuery):

    user_id = callback_query.from_user.id

    await update_user_state(
        user_id,
        {
            "waiting_for_repo": True
        }
    )

    await callback_query.message.reply_text(
        "📦 Send GitHub repository URL.\n\n"
        "Example:\n"
        "https://github.com/username/repository"
    )

    await callback_query.answer()


@Client.on_message(filters.text & filters.private)
async def receive_repo(client, message: Message):

    user_id = message.from_user.id

    user = await get_user(user_id)

    if not user:
        return

    waiting = user.get("waiting_for_repo")

    if not waiting:
        return

    text = message.text.strip()

    pattern = r"^https:\/\/github\.com\/[\w.-]+\/[\w.-]+\/?$"

    if not re.match(pattern, text):

        return await message.reply_text(
            "❌ Invalid GitHub repository URL."
        )

    await update_user_state(
        user_id,
        {
            "waiting_for_repo": False
        }
    )

    await message.reply_text(
        f"✅ Repository received:\n\n{text}"
    )
