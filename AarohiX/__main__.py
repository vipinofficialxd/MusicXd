import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AarohiX import LOGGER, app, userbot
from AarohiX.core.call import Aarohi
from AarohiX.plugins import ALL_MODULES
from AarohiX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("AarohiX").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("AarohiX").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AarohiX.plugins." + all_module)
    LOGGER("AarohiX.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Aarohi.start()
    try:
        await Aarohi.stream_decall("https://telegra.ph/file/7839f4020a6f6b1690aac.jpg")
    except:
        pass
    try:
        await Aarohi.stream_call(
            "https://telegra.ph/file/7839f4020a6f6b1690aac.jpg"
        )
    except NoActiveGroupCall:
        LOGGER("AarohiX").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Aarohi.decorators()
    LOGGER("AarohiX").info("Aarohi X Music")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AarohiX").info("Stopping Music Bot...")
