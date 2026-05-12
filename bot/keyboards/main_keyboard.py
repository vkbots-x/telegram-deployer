from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_keyboard():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🚀 Deploy Bot",
                callback_data="deploy_menu"
            )
        ],
        [
            InlineKeyboardButton(
                "🔑 API Tokens",
                callback_data="api_tokens_menu"
            )
        ],
        [
            InlineKeyboardButton(
                "📁 My Projects",
                callback_data="projects_menu"
            )
        ],
        [
            InlineKeyboardButton(
                "❓ Help",
                callback_data="help_menu"
            )
        ]
        [
        InlineKeyboardButton(
    "🚀 Deploy Bot",
    callback_data="deploy_bot"
        )]
    ])
