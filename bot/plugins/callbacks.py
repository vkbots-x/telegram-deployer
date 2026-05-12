from pyrogram import Client, filters

from bot.keyboards.main_keyboard import main_keyboard


# ---------------- DEPLOY ---------------- #

@Client.on_callback_query(filters.regex("^deploy_menu$"))
async def deploy_menu_callback(client, callback_query):

    try:

        await callback_query.answer()

        text = """
🚀 Deploy Bot

Supported Platforms:

• Render
• Koyeb
• Heroku

Deployment system will be available soon.
"""

        await callback_query.message.edit_text(
            text=text,
            reply_markup=main_keyboard()
        )

    except Exception as e:
        print(f"DEPLOY CALLBACK ERROR: {e}")


# ---------------- API TOKENS ---------------- #

@Client.on_callback_query(filters.regex("^api_tokens_menu$"))
async def api_tokens_callback(client, callback_query):

    try:

        await callback_query.answer()

        text = """
🔑 API Tokens

Available Commands:

/setgithub - Set GitHub token
/setkoyeb - Set Koyeb token

More providers coming soon.
"""

        await callback_query.message.edit_text(
            text=text,
            reply_markup=main_keyboard()
        )

    except Exception as e:
        print(f"API TOKENS CALLBACK ERROR: {e}")


# ---------------- PROJECTS ---------------- #

@Client.on_callback_query(filters.regex("^projects_menu$"))
async def projects_callback(client, callback_query):

    try:

        await callback_query.answer()

        text = """
📁 My Projects

No deployed projects found.
"""

        await callback_query.message.edit_text(
            text=text,
            reply_markup=main_keyboard()
        )

    except Exception as e:
        print(f"PROJECTS CALLBACK ERROR: {e}")


# ---------------- HELP ---------------- #

@Client.on_callback_query(filters.regex("^help_menu$"))
async def help_callback(client, callback_query):

    try:

        await callback_query.answer()

        text = """
📚 Available Commands

/start - Start bot
/help - Show help

/setgithub - Set GitHub token
/setkoyeb - Set Koyeb token

More deployment features coming soon.
"""

        await callback_query.message.edit_text(
            text=text,
            reply_markup=main_keyboard()
        )

    except Exception as e:
        print(f"HELP CALLBACK ERROR: {e}")
