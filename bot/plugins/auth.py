from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from database.users import update_user_token
from utils.encryption import encrypt_text


@Client.on_message(filters.command("setgithub"))
async def set_github_token(
    client: Client,
    message: Message
):

    user_id = message.from_user.id

    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:
        return await message.reply_text(
            "Usage:\n/setgithub YOUR_TOKEN"
        )

    token = parts[1]

    encrypted = encrypt_text(token)

    await update_user_token(
        user_id,
        "github_token",
        encrypted
    )

    await message.reply_text(
        "✅ GitHub token saved securely."
    )


@Client.on_message(filters.command("setkoyeb"))
async def set_koyeb_token(
    client: Client,
    message: Message
):

    user_id = message.from_user.id

    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:
        return await message.reply_text(
            "Usage:\n/setkoyeb YOUR_TOKEN"
        )

    token = parts[1]

    encrypted = encrypt_text(token)

    await update_user_token(
        user_id,
        "koyeb_token",
        encrypted
    )

    await message.reply_text(
        "✅ Koyeb token saved securely."
    )
