import asyncio
import requests
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pyrogram import Client as Bot
from modules.config import arq, API_ID, API_HASH, BOT_TOKEN, BG_IMAGE, bot

response = requests.get(BG_IMAGE)
with open("./resource/thumbnail.png", "wb") as file:
    file.write(response.content)
    

call_py = PyTgCalls(bot)
                    
                    

async def main():
    await call_py.start()
    print(
        """
    ------------------
   | Userbot Actived! |
    ------------------
"""
    )
    await idle()
    await arq.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
