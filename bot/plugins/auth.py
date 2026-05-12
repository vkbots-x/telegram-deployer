from pyrogram import Client, filters
from pyrogram.types import Message

from database.users import (
    update_user_token,
    update_user_state,
    get_user
)

from utils.encryption import encrypt_text
from services.github_token import validate_github_token


@Client.on_message(filters.command("setgithub"))
async def set_github_token(client, message: Message):

    user_id = message.from_user.id

    await update_user_state(
        user_id,
        {
            "waiting_for_token": "github"
        }
    )

    await message.reply_text(
        "🔑 Send your GitHub token."
    )


@Client.on_message(filters.command("setkoyeb"))
async def set_koyeb_token(client, message: Message):

    user_id = message.from_user.id

    await update_user_state(
        user_id,
        {
            "waiting_for_token": "koyeb"
        }
    )

    await message.reply_text(
        "🔑 Send your Koyeb token."
    )


@Client.on_message(filters.text & filters.private)
async def receive_tokens(client, message: Message):

    user_id = message.from_user.id

    user = await get_user(user_id)

    if not user:
        return

    waiting = user.get("waiting_for_token")

    if not waiting:
        return

    token = message.text.strip()

    # =========================
    # GITHUB TOKEN
    # =========================

    if waiting == "github":

        valid = await validate_github_token(token)

        if not valid:
            return await message.reply_text(
                "❌ Invalid GitHub token."
            )

        encrypted = encrypt_text(token)

        await update_user_token(
            user_id,
            "github_token",
            encrypted
        )

        await update_user_state(
            user_id,
            {
                "waiting_for_token": None
            }
        )

        return await message.reply_text(
            "✅ GitHub token saved successfully."
        )

    # =========================
    # KOYEB TOKEN
    # =========================

    if waiting == "koyeb":

        encrypted = encrypt_text(token)

        await update_user_token(
            user_id,
            "koyeb_token",
            encrypted
        )

        await update_user_state(
            user_id,
            {
                "waiting_for_token": None
            }
        )

        return await message.reply_text(
            "✅ Koyeb token saved successfully."
        )
