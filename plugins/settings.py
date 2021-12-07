# (c) @AbirHasan2005
from pyrogram import Client, filters
import asyncio
from pyrogram import types, errors
from sample_config import Config


@Client.on_message(filters.private & filters.command("settings"))
async def show_settings(m: "types.Message"):
    upload_as_doc = user_data.get("upload_as_doc", False)
    caption = user_data.get("caption", None)
    apply_caption = user_data.get("apply_caption", True)
    thumbnail = user_data.get("thumbnail", None)
    buttons_markup = [
        [types.InlineKeyboardButton(f"Upload as Doc {'✅' if upload_as_doc else '❌'}",
                                    callback_data="triggerUploadMode")],
        [types.InlineKeyboardButton(f"Apply Caption {'✅' if apply_caption else '❌'}",
                                    callback_data="triggerApplyCaption")],
        [types.InlineKeyboardButton(f"Apply Default Caption {'❌' if caption else '✅'}",
                                    callback_data="triggerApplyDefaultCaption")],
        [types.InlineKeyboardButton("Set Custom Caption",
                                    callback_data="setCustomCaption")],
        [types.InlineKeyboardButton(f"{'Change' if thumbnail else 'Set'} Thumbnail",
                                    callback_data="setThumbnail")]
    ]
    if thumbnail:
        buttons_markup.append([types.InlineKeyboardButton("Show Thumbnail",
                                                          callback_data="showThumbnail")])
    if caption:
        buttons_markup.append([types.InlineKeyboardButton("Show Caption",
                                                          callback_data="showCaption")])
    buttons_markup.append([types.InlineKeyboardButton("Close Message",

