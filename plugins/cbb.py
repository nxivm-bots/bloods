# https://t.me/Ultroid_Official/524

from pyrogram import __version__, Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ParseMode
from database.database import full_userbase
from bot import Bot
from config import OWNER_ID, ADMINS, CHANNEL, SUPPORT_GROUP, OWNER
from plugins.cmd import *

# Callback query handler
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data

    if data == "about":
        await query.message.edit_text(
            text=f"ㅤㅤㅤ⌠ 𝗕𝗹𝗼𝗼𝗱𝘀 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 🍀⌡\n\n"
                 f"◉ Bʟᴏᴏᴅs Sɪᴛᴇʀɪᴘ - @{CHANNEL}\n"
                 f"◉ Bʟᴏᴏᴅs Oɴʟʏғᴀɴs - @{SUPPORT_GROUP}</b>"
                 f"◉ Cʀᴇᴀᴛᴇʀ - <a href='tg://user?id={OWNER_ID}'>Saint</a>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔒 Close", callback_data="close")]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception as e:
            print(f"Error deleting reply-to message: {e}")

    elif data == "upi_info":
        await upi_info(client, query.message)

    elif data == "show_plans":
        await show_plans(client, query.message)

# https://t.me/Ultroid_Official/524


# ultroidofficial : YT
