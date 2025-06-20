from pyrogram.types import InlineKeyboardButton, WebAppInfo

import config
from YTMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_10"],
                url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_12"], callback_data="abot_cb"),
            InlineKeyboardButton(text=_["S_B_13"], callback_data="ubot_cb"),
        ],
        [
            InlineKeyboardButton("ᴘɪɴɢ 💌", callback_data="ping_popup"),
            InlineKeyboardButton(
                text="ɢɪᴛʜᴜʙ 🗨️",
                web_app=WebAppInfo(
                    url="https://github.com/NoxxOP?tab=repositories"
                )
            )
        ]
    ]
    return buttons
