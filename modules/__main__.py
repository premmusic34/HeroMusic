import asyncio
from pytgcalls import idle
from modules.clientbot import call_py, bot, user
from modules.config import arq


async def start_bot():
    await bot.start()
    print("[INFO]: BOT & UBOT CLIENT STARTED !!")
    await call_py.start()
    print("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await user.join_chat("AdityaServer")
    await user.join_chat("HeroOfficialBots")
    await user.join_chat("baddies2buddies")
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await arq.close()
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
