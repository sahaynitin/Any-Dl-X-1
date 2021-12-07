import pyrogram
from pyrogram import Client, filters

async def settings_handler(bot: Client, m: Message):
    editable = await m.reply_text("Please Wait ...", quote=True)
    await OpenSettings(editable, m.from_user.id)
@Client.on_message(filters.private & filters.command("settings"))
async def settings_handler(bot: Client, m: Message):
    editable = await m.reply_text("Please Wait ...", quote=True)
    await OpenSettings(editable, m.from_user.id)
