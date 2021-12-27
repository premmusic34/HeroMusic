import asyncio
import requests
from pytgcalls import idle
from modules.config import arq, BG_IMAGE, call_py

response = requests.get(BG_IMAGE)
with open("./resource/thumbnail.png", "wb") as file:
    file.write(response.content)
    


                    

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
