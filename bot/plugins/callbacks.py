from pyrogram import Client, filters


@Client.on_callback_query(filters.regex("^deploy_bot$"))
async def deploy_bot_callback(client, callback_query):

    await callback_query.answer()

    await callback_query.message.edit_text(
        "🚀 Deployment system coming soon."
    )


@Client.on_callback_query(filters.regex("^api_tokens$"))
async def api_tokens_callback(client, callback_query):

    await callback_query.answer()

    await callback_query.message.edit_text(
        "🔑 API token manager coming soon."
    )


@Client.on_callback_query(filters.regex("^my_projects$"))
async def my_projects_callback(client, callback_query):

    await callback_query.answer()

    await callback_query.message.edit_text(
        "📁 Project dashboard coming soon."
    )


@Client.on_callback_query(filters.regex("^help$"))
async def help_callback(client, callback_query):

    await callback_query.answer()

    await callback_query.message.edit_text(
        """
📚 Available Commands

/start - Start bot
/help - Show help

/setgithub - Set GitHub token
/setkoyeb - Set Koyeb token
"""
    )
