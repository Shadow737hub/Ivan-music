# userbot.py
from pyrogram import Client
from misc import logger

# Replace with your actual string session (from config.py or env)
from config import STRING_SESSION

# Create userbot client
userbot = Client(
    name="userbot",
    session_string=STRING_SESSION,
    api_id=123456,       # your api_id from my.telegram.org
    api_hash="your_api_hash"
)

async def start_userbot():
    await userbot.start()
    me = await userbot.get_me()
    logger.info(f"Userbot started as {me.first_name} (@{me.username})")

async def stop_userbot():
    await userbot.stop()
    logger.info("Userbot stopped.")
