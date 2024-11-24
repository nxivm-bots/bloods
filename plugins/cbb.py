

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

    elif data == "premium":
        await query.message.edit_text(
            text="Choose an option:",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Buy Silver", callback_data="buy_silver")],
                    [InlineKeyboardButton("Buy Gold", callback_data="buy_gold")],
                    [InlineKeyboardButton("Buy Diamond", callback_data="buy_diamond")],
                    [InlineKeyboardButton("Close", callback_data="close")]
                ]
            )
        )
    elif data == "buy_silver":
        await query.message.edit_text(
            text=(
                "<b><u>Silver Plan</u></b>\n\n"
                "1 Month - 50 INR\n"
                "<pre>≡ This plan provides premium access for our current bot with no Ads.</pre>\n"
                "⩉ <a href='https://i.ibb.co/BCGJBvd/file-2330.jpg'>Click To Get QR</a>\n"
                "⌕ For other payment methods, contact @odacchi.\n\n"
                "<b>Note: This plan is separate and lets you use bots without verification (Ads) only. Limits will remain the same as before.</b>"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Back", callback_data="premium")],
                    [InlineKeyboardButton("Close", callback_data="close")]
                ]
            )
        )
    elif data == "buy_gold":
        await query.message.edit_text(
            text=(
                "<b><u>Gold Plan</u></b>\n\n"
                "1 Month - 100 INR\n"
                "<pre>≡ This plan provides premium access for our two bots with no Ads.</pre>\n"
                "⩉ <a href='https://i.ibb.co/BCGJBvd/file-2330.jpg'>Click To Get QR</a>\n"
                "⌕ For other payment methods, contact @odacchi.\n\n"
                "<b>Note: This plan offers enhanced limits and fewer restrictions.</b>"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Back", callback_data="premium")],
                    [InlineKeyboardButton("Close", callback_data="close")]
                ]
            )
        )
    elif data == "buy_diamond":
        await query.message.edit_text(
            text=(
                "<b>Diamond Plan</b>\n\n"
                "1 Month - 150 INR\n"
                "<pre>≡ This plan provides premium access for our bots with no Ads.</pre>\n"
                "⩉<a href='https://i.ibb.co/BCGJBvd/file-2330.jpg'>Click To Get QR</a>\n"
                "⌕ For other payment methods, contact @odacchi.\n\n"
                "<b>Note: This plan is separate and lets you use bots without verification (Ads) only. Limits will remain the same as before.</b>"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Back", callback_data="premium")],
                    [InlineKeyboardButton("Close", callback_data="close")]
                ]
            )
        )

    elif data == "show_plans":
        await show_plans(client, query.message)
