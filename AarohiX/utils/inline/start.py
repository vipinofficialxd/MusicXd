from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ [❤‍🔥ᴅɪʟ❤‍🔥] 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️ʜᴇʟᴩ❣️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 ᴏᴡɴᴇʀ 💖", url=f"https://t.me/sexyaaditya"),
            InlineKeyboardButton(
                text="🥰 ᴄᴏ ᴏᴡɴᴇʀ[❣️] 🥰", url=f"https://t.me/sexyvipin"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[xᴅ]💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ[ᴅᴀʙᴀɴɢ]🥰", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ [💞ᴅᴀʙᴀɴɢ💞]🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺ʜᴇʟᴩ🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 ᴏᴡɴᴇʀ 💖", url=f"https://t.me/sexyaaditya"),
            InlineKeyboardButton(
                text="🥰 ᴄᴏ ᴏᴡɴᴇʀ[❣️] 🥰", url=f"https://t.me/sexyvipin"
            ),
        ],
        [
            InlineKeyboardButton(text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[xᴅ]💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ[ᴅᴀʙᴀɴɢ]🥰", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🥰 ᴏᴡɴᴇʀ 🥰", url=f"https://t.me/sexyaaditya"
                )
        ],
     ]
    return buttons
