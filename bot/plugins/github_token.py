import aiohttp

from pyrogram import Client, filters
from pyrogram.types import Message

from database.states import user_states
from database.tokens import save_github_token


# ---------------- VALIDATE TOKEN ---------------- #

async def validate_github_token(token: str):

    url = "https://api.github.com/user"

    headers = {
        "Authorization": f"token {token}"
    }

    try:

        async with aiohttp.ClientSession() as session:

            async with session.get(
                url,
                headers=headers
            ) as response:

                if response.status == 200:

                    data = await response.json()

                    return True, data.get("login")

                return False, None

    except Exception as e:

        print(f"GITHUB VALIDATION ERROR: {e}")

        return False, None


# ---------------- COMMAND ---------------- #

@Client.on_message(filters.command(["setgithub"]))
async def set_github_command(client, message: Message):

    user_id = message.from_user.id

    user_states[user_id] = "waiting_github_token"

    await message.reply_text(
        """
🔑 Send your GitHub Personal Access Token.

Your token will be verified before saving.
"""
    )


# ---------------- TOKEN RECEIVER ---------------- #

@Client.on_message(filters.text & ~filters.command(["start", "help", "setgithub"]))
async def github_token_receiver(client, message: Message):

    user_id = message.from_user.id

    state = user_states.get(user_id)

    if state != "waiting_github_token":
        return

    token = message.text.strip()

    await message.reply_text(
        "🔍 Verifying GitHub token..."
    )

    valid, username = await validate_github_token(token)

    if not valid:

        await message.reply_text(
            """
❌ Invalid GitHub token.

Please send a valid Personal Access Token.
"""
        )

        return

    await save_github_token(user_id, token)

    user_states.pop(user_id, None)

    await message.reply_text(
        f"""
✅ GitHub token verified successfully.

👤 GitHub Username: `{username}`
"""
    )
