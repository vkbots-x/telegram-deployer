from pyrogram import Client, filters
from pyrogram.types import Message

from database.users import update_user_token
from database.states import user_states

from services.github_token import validate_github_token


@Client.on_message(filters.command(["setgithub"]))
async def set_github_token(
    client: Client,
    message: Message
):

    user_id = message.from_user.id

    user_states[user_id] = "waiting_github_token"

    await message.reply_text(
        """
🔑 Send your GitHub Personal Access Token.

Your token will be verified before saving.
"""
    )


@Client.on_message(filters.command(["setkoyeb"]))
async def set_koyeb_token(
    client: Client,
    message: Message
):

    user_id = message.from_user.id

    user_states[user_id] = "waiting_koyeb_token"

    await message.reply_text(
        """
🔑 Send your Koyeb API Token.
"""
    )


@Client.on_message(
    filters.text
    & ~filters.command(
        [
            "start",
            "help",
            "setgithub",
            "setkoyeb"
        ]
    )
)
async def receive_tokens(
    client: Client,
    message: Message
):

    user_id = message.from_user.id

    state = user_states.get(user_id)

    if not state:
        return

    token = message.text.strip()

    # ---------------- GITHUB ---------------- #

    if state == "waiting_github_token":

        checking = await message.reply_text(
            "🔍 Verifying GitHub token..."
        )

        valid, username = await validate_github_token(token)

        if not valid:

            user_states.pop(user_id, None)

            return await checking.edit_text(
                """
❌ Invalid GitHub token.

Try again using:

/setgithub
"""
            )

        await update_user_token(
            user_id,
            "github_token",
            token
        )

        user_states.pop(user_id, None)

        return await checking.edit_text(
            f"""
✅ GitHub token verified successfully.

👤 Username: `{username}`
"""
        )

    # ---------------- KOYEB ---------------- #

    if state == "waiting_koyeb_token":

        await update_user_token(
            user_id,
            "koyeb_token",
            token
        )

        user_states.pop(user_id, None)

        return await message.reply_text(
            "✅ Koyeb token saved successfully."
        )
