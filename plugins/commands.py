import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from sample_config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
@Client.on_message(filters.command(["start", "ping"]) & filters.private & ~filters.edited)
async def ping_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await m.reply_text("Hi, I am Rename Bot!\n\n"
                       "I can rename media without downloading it!\n"
                       "Speed depends on your media DC.\n\n"
                       "Just send me media and reply to it with /rename command.",
                       reply_markup=types.InlineKeyboardMarkup([[
                           types.InlineKeyboardButton("Show Settings",
                                                      callback_data="showSettings")
                       ]]))
