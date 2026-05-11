from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton


def main_keyboard():

    buttons = [
        [
            InlineKeyboardButton(
                "🚀 Deploy Bot",
                callback_data="deploy_menu"
            )
        ],
        [
            InlineKeyboardButton(
                "🔑 API Tokens",
                callback_data="api_tokens"
            )
        ],
        [
            InlineKeyboardButton(
                "📦 My Projects",
                callback_data="my_projects"
            )
        ],
        [
            InlineKeyboardButton(
                "🛠 Help",
                callback_data="help_menu"
            )
        ]
    ]

    return InlineKeyboardMarkup(buttons)
