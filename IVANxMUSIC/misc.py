# misc.py
# Made by Ivan

import asyncio
import logging
import random
import string
import os
from datetime import datetime, timedelta

from pymongo import MongoClient
import socket
import config  # <-- Must have: MONGO_URI, HEROKU_APP_NAME, HEROKU_API_KEY

import heroku3  # pip install heroku3

# ✅ Logger setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("MusicBot")

# ✅ Heroku
HEROKU_APP_NAME = config.HEROKU_APP_NAME
HEROKU_API_KEY = config.HEROKU_API_KEY

heroku_conn = heroku3.from_key(HEROKU_API_KEY)
heroku_app = None
if HEROKU_APP_NAME:
    try:
        heroku_app = heroku_conn.apps()[HEROKU_APP_NAME]
    except Exception as e:
        logger.warning(f"Could not connect to Heroku app: {e}")

# ✅ MongoDB connection
mongo_client = MongoClient(config.MONGO_URI)
db = mongo_client.get_default_database()

# ✅ List of user IDs who have SUDO permissions
SUDO_USERS = [123456789, 987654321]  # Replace with your Telegram user IDs

# ✅ Assistant start message
ASSISTANT_START_MSG = f"""
✨ **Telegram Music Bot Started!**
✅ Use /play <song name> to stream music.
⚙️ Powered by Python & Pyrogram.
☁️ Deployed on Heroku as `{HEROKU_APP_NAME}`
🖥 Host: `{socket.gethostname()}`
👤 Made by Ivan.
"""

# === Time helpers ===
def current_utc_time() -> datetime:
    """
    Return current UTC datetime.
    """
    return datetime.utcnow()

def formatted_time() -> str:
    """
    Return formatted current time as string.
    """
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

def uptime(start_time: datetime) -> str:
    """
    Return human-readable uptime from start_time.
    """
    delta = datetime.utcnow() - start_time
    return str(delta).split('.')[0]

# === Socket helpers ===
def get_hostname() -> str:
    """
    Return system hostname.
    """
    return socket.gethostname()

def is_connected(host="8.8.8.8", port=53, timeout=3) -> bool:
    """
    Check if we have internet connection.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception:
        return False

# === Heroku helpers ===
def restart_heroku_app():
    """
    Restart the Heroku app dynos.
    """
    if heroku_app:
        heroku_app.restart()
        logger.info("Heroku app restarted successfully!")
    else:
        logger.warning("Heroku app not configured; cannot restart.")

# === Other utilities ===
def format_duration(seconds: int) -> str:
    return str(timedelta(seconds=seconds))

def format_file_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(min(len(size_name) - 1, (size_bytes).bit_length() / 10))
    p = pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def generate_random_string(length: int = 10) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

async def safe_sleep(delay: float, reason: str = None):
    if reason:
        logger.info(f"Sleeping for {delay} seconds: {reason}")
    await asyncio.sleep(delay)

def get_file_extension(filename: str) -> str:
    return os.path.splitext(filename)[1][1:].lower()

def clean_title(text: str) -> str:
    return text.replace('_', ' ').replace('-', ' ').strip().title()

# Add more helpers below as needed
