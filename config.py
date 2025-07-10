
# config.py

import os

class Config:
    # Telegram API credentials (from https://my.telegram.org)
    API_ID = int(os.getenv("API_ID", "12345678"))
    API_HASH = os.getenv("API_HASH", "your_api_hash_here")

    # Bot token from BotFather
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")

    # String session for userbot / assistant (generate with Pyrogram)
    STRING_SESSION = os.getenv("STRING_SESSION", "your_string_session_here")

    # MongoDB URI (for database)
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://user:pass@cluster.mongodb.net/dbname")

    # Your Telegram user ID (bot owner)
    OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

    # Log channel / group ID (for bot logs)
    LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1001234567890"))

    # Support channel (for updates)
    SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/YourSupportChannel")

    # Support chat group (for user help)
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/YourSupportChat")

    # Song duration limit in minutes
    DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", "10"))

    # PyTgCalls audio quality
    AUDIO_QUALITY = os.getenv("AUDIO_QUALITY", "high")
