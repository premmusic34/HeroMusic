import os
import sys
from pyrogram.types import Message
from modules.helpers.filters import command
from pyrogram import Client
from os import system, execle, environ
from modules.helpers.decorators import errors, sudo_users_only


@Client.on_message(command(["/restart", "R", "/restart@{BOT_USERNAME}"]))
@errors
@sudo_users_only
async def restart_bot(_, message: Message):
    msg = await message.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
    args = [sys.executable, "main.py"]
    await msg.edit("✅ ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ...\n✅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴀғᴛᴇʀ 𝟷 ᴍɪɴᴜᴛᴇ ")
    execle(sys.executable, *args, environ)
    return