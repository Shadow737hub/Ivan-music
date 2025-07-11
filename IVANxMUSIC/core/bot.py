# bot.py
from pyrogram import Client, filters
from misc import (
    logger,
    SUDO_USERS,
    restart_heroku_app,
    current_utc_time,
    uptime as get_uptime,
    ASSISTANT_START_MSG
)

start_time = current_utc_time()
app = Client("musicbot")


@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(ASSISTANT_START_MSG)


@app.on_message(filters.command("restart") & filters.user(SUDO_USERS))
async def restart_cmd(client, message):
    await message.reply_text("♻️ Restarting the bot on Heroku...")
    logger.info(f"Restart command triggered by user: {message.from_user.id}")
    restart_heroku_app()


@app.on_message(filters.command("uptime") & filters.user(SUDO_USERS))
async def uptime_cmd(client, message):
    up = get_uptime(start_time)
    await message.reply_text(f"✅ Bot uptime: `{up}`")


@app.on_message(filters.command("ping"))
async def ping_cmd(client, message):
    import time
    start = time.time()
    m = await message.reply_text("🏓 Pinging...")
    end = time.time()
    latency = (end - start) * 1000
    await m.edit_text(f"🏓 Pong! `{int(latency)}ms`")


@app.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("""
**🤖 Available Commands:**
/start - Show welcome message
/help - Show this help
/ping - Check if bot is alive
/restart - Restart the bot (sudo only)
/uptime - Show bot uptime (sudo only)
""")


app.run()

