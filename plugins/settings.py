# (c) @AbirHasan2005

import asyncio
from pyrogram.errors import MessageNotModified, FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def OpenSettings(m: Message, user_id: int):
    try:
        await m.edit(
            text="Here You Can Change or Configure Your Settings:",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Show Thumbnail", callback_data="showThumbnail")],
                    [InlineKeyboardButton("Show Queue Files", callback_data="showQueueFiles")],
                    [InlineKeyboardButton("Close", callback_data="closeMeh")]
                ]
            )
        )
    except MessageNotModified:
        pass
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await m.edit("You Are Spamming!")
    except Exception as err:
        raise err
