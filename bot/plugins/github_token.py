from pyrogram import Client, filters
from pyrogram.types import Message

from database.states import user_states
from database.tokens import save_github_token


# ---------------- COMMAND ---------------- #

@Client.on_message(filters.command(["setgithub"]))
async def set_github_command(client, message: Message):

    user_id = message.from_user.id

    user_states[user_id] = "waiting_github_token"

    await message.reply_text(
        """
🔑 Send your GitHub Personal Access Token.

Your token will be stored securely.
"""
    )


# ---------------- TOKEN RECEIVER ---------------- #

@Client.on_message(filters.text & ~filters.command(["start", "help"]))
async def github_token_receiver(client, message: Message):

    user_id = message.from_user.id

    state = user_states.get(user_id)

    if state != "waiting_github_token":
        return

    token = message.text.strip()

    # Basic validation
    if len(token) < 20:

        await message.reply_text(
            "❌ Invalid GitHub token."
        )

        return

    await save_github_token(user_id, token)

    user_states.pop(user_id, None)

    await message.reply_text(
        "✅ GitHub token saved successfully."
    )
