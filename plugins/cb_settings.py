@ScreenShotBot.on_message(filters.private & filters.command("settings"))
async def start(c, m):

    await Utilities.display_settings(c, m, db)
