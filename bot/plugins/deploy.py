from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    Message
)

from database.states import user_states
from database.users import get_user

from services.github_repo import (
    validate_repo_access,
    get_authenticated_user,
    fork_repository
)


@Client.on_callback_query(
    filters.regex("^deploy_bot$")
)
async def deploy_button(
    client: Client,
    callback_query: CallbackQuery
):

    user_id = callback_query.from_user.id

    user = await get_user(user_id)

    if not user:

        return await callback_query.message.reply_text(
            "User not found."
        )

    github_token = user.get("github_token")

    if not github_token:

        return await callback_query.message.reply_text(
            """
❌ GitHub token not set.

Use:
/setgithub TOKEN
"""
        )

    user_states[user_id] = "waiting_repo"

    await callback_query.message.reply_text(
        """
📦 Send GitHub repository URL.

Example:
https://github.com/username/repository
"""
    )

    await callback_query.answer()


@Client.on_message(filters.text)
async def receive_repo(
    client: Client,
    message: Message
):

    user_id = message.from_user.id

    state = user_states.get(user_id)

    if state != "waiting_repo":
        return

    repo_url = message.text.strip()

    user = await get_user(user_id)

    github_token = user.get("github_token")

    checking = await message.reply_text(
        "🔍 Checking repository..."
    )

    valid, repo_data = await validate_repo_access(
        github_token,
        repo_url
    )

    if not valid:

        user_states.pop(user_id, None)

        return await checking.edit_text(
            """
❌ Invalid repository.

Please try again.
"""
        )

    authenticated_user = await get_authenticated_user(
        github_token
    )

    repo_owner = repo_data["owner"]["login"]

    # USER ALREADY OWNS REPO

    if authenticated_user.lower() == repo_owner.lower():

        user_states.pop(user_id, None)

        return await checking.edit_text(
            f"""
✅ Repository verified.

📦 Repo:
{repo_data['full_name']}

You already own this repository.

Deployment flow coming next.
"""
        )

    # FORK REQUIRED

    await checking.edit_text(
        "🍴 Forking repository..."
    )

    forked = await fork_repository(
        github_token,
        repo_url
    )

    user_states.pop(user_id, None)

    if not forked:

        return await checking.edit_text(
            """
❌ Failed to fork repository.
"""
        )

    await checking.edit_text(
        f"""
✅ Repository forked successfully.

📦 Original:
{repo_data['full_name']}

🚀 Ready for deployment flow.
"""
    )
