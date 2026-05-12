from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):

    text = """
📚 Available Commands

/start - Start bot
/help - Show help

/setgithub - Set GitHub token
/setkoyeb - Set Koyeb token
"""

    await message.reply_text(text)
