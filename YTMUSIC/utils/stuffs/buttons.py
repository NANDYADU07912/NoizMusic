
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# --- Button Class ---
class BUTTONS(object):
    ABUTTON = [
        [InlineKeyboardButton("🛠️ ˹ sᴜᴘᴘᴏꝛᴛ ˼", url="https://t.me/ShrutiBotSupport")],
        [InlineKeyboardButton("📢 ˹ ᴜᴘᴅᴧᴛᴇ ˼", url="https://t.me/ShrutiBots"),
         InlineKeyboardButton("˹ ❍ᴡɴᴇꝛ ˼", user_id=7674874652),
         InlineKeyboardButton("🤖 ˹ ᴧʟʟ ʙᴏᴛ ˼", url="https://t.me/ShrutiAllBots")],
        [InlineKeyboardButton("🔙 ↺ ʙᴧᴄᴋ ↻", callback_data="settingsback_helper")]
    ]

    UBUTTON = [
        [InlineKeyboardButton("🎵 ˹ ᴍᴜsɪᴄ ˼", callback_data="settings_back_helper"),
         InlineKeyboardButton("🧰 ˹ ᴛᴏᴏʟs ˼", callback_data="tbot_cb")],
        [InlineKeyboardButton("⚙️ ˹ ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ˼", callback_data="dplus HELP_host")],
        [InlineKeyboardButton("🔙 ↺ ʙᴧᴄᴋ ↻", callback_data="settingsback_helper")]
    ]

    TBUTTON = [  
        [InlineKeyboardButton("🟢 ˹ ᴀᴄᴛɪᴠᴇ ˼", callback_data="cplus HELP_active"),  
         InlineKeyboardButton("🔐 ˹ ᴀᴜᴛʜ ˼", callback_data="cplus HELP_auth")],  
        [InlineKeyboardButton("🚫 ˹ ʙʟᴏᴄᴋ ˼", callback_data="cplus HELP_block"),  
         InlineKeyboardButton("👨‍💻 ˹ ᴅᴇᴠ ˼", callback_data="cplus HELP_dev")],  
        [InlineKeyboardButton("📡 ˹ ɢ-ᴄᴀsᴛ ˼", callback_data="cplus HELP_gcast"),  
         InlineKeyboardButton("💬 𝐂ʜᴀᴛʙᴏᴛ ʜᴇʟᴘ", callback_data="chatbot_help")],  
        [InlineKeyboardButton("📂 𝐁ᴏᴛ ʀᴇᴘᴏ", url="https://github.com/NoxxOP/ShrutiMusic/fork"),
         InlineKeyboardButton("🔙 ↺ ʙᴧᴄᴋ ↻", callback_data="ubot_cb")]  
    ]
