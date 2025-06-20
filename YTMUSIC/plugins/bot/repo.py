from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from YTMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹ sʜʀᴜᴛɪ-ᴍᴜsɪᴄ ˼ ʙᴏᴛ ✪

❍ • ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ ᴀɴᴅ ᴇɴᴊᴏʏ 🎧

❍ • sᴜᴘᴘᴏʀᴛ : @ShrutiBots
❍ • ᴏᴡɴᴇʀ : @WTF_WHYMeeh
❍ • ɢʀᴏᴜᴘ : @ShrutiBotSupport
**"""

# Command triggers
REPO_COMMANDS = ["repo", "source"]

@app.on_message(filters.command(REPO_COMMANDS, prefixes=["/", ".", "!"]))
async def repo_source_handler(_, msg):
    buttons = [
        [InlineKeyboardButton("•ᴀᴅᴅ ᴍᴇ•", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("•ʀᴇᴘᴏ•", url="https://github.com/NoxxOP/ShrutiMusic/fork"),
            InlineKeyboardButton("•ᴏᴡɴᴇʀ•", url="https://t.me/WTF_WHYMeeh"),
        ],
        [
            InlineKeyboardButton("•sᴜᴘᴘᴏʀᴛ•", url="https://t.me/ShrutiBotSupport"),
            InlineKeyboardButton("•ᴄʜᴀɴɴᴇʟ•", url="https://t.me/ShrutiBots"),
        ],
        [
            InlineKeyboardButton("•sʜʀᴜᴛɪxʀᴏʙᴏᴛ•", url="https://t.me/ShrutixRobot"),
            InlineKeyboardButton("•sʜʀᴜᴛɪxᴄʜᴀᴛʙᴏᴛ•", url="https://t.me/ShrutixChatbot"),
        ],
        [
            InlineKeyboardButton("•ʙʟᴜsʜ-ᴍᴜsɪᴄ•", url="https://t.me/BlushMusicbot"),
            InlineKeyboardButton("•sʜʀᴜᴛɪx-ᴍᴜsɪᴄ•", url="https://t.me/ShrutixMusicBot"),
        ],
        [
            InlineKeyboardButton("•ᴍᴜsɪᴄ4ᴠᴄ•", url="https://t.me/Music4vcbot"),
            InlineKeyboardButton("•ᴏᴘᴀʟx-ʙᴏᴛ•", url="https://t.me/Opalxbot"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_text(
        text=start_txt,
        reply_markup=reply_markup
    )
