# Made By Ivan - @x8Ahad
Dont Copy And Sell this repo Thanks
# config.py

import os
import re
from dotenv import load_dotenv
from pyrogram import filters


class Config:
    # Telegram API credentials (from https://my.telegram.org)
    API_ID = int(os.getenv("API_ID", "28209312"))
    API_HASH = os.getenv("API_HASH", "89def84a7894bb696ff20174c86889a4")

    # Bot token from BotFather
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")

    # String session for userbot / assistant (generate with Pyrogram)
    STRING_SESSION = os.getenv("STRING_SESSION", "your_string_session_here")

    # MongoDB URI (for database)
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://ahaan:ahaad@ahaan.hgkeruq.mongodb.net/?retryWrites=true&w=majority&appName=ahaan")

    # Your Telegram user ID (bot owner)
    OWNER_ID = int(os.getenv("OWNER_ID", "7550591956"))

    # Log channel / group ID (for bot logs)
    LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1002759072638"))

    # Support channel (for updates)
    SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/+7242s4ZFgaNiODM1")

    # Support chat group (for user help)
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/+m63eJ-Mc_jpjMzll")

    # Song duration limit in minutes
    DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", "10000"))

    # PyTgCalls audio quality
    AUDIO_QUALITY = os.getenv("AUDIO_QUALITY", "high")
