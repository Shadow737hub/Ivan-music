# afkdb.py
from misc import db, logger
from datetime import datetime

afk_collection = db["afk"]  # collection named 'afk'

def set_afk(user_id: int, reason: str = "AFK"):
    """
    Mark user as AFK.
    """
    afk_collection.update_one(
        {"user_id": user_id},
        {"$set": {"reason": reason, "since": datetime.utcnow()}},
        upsert=True
    )
    logger.info(f"User {user_id} set as AFK: {reason}")

def remove_afk(user_id: int):
    """
    Remove AFK status.
    """
    afk_collection.delete_one({"user_id": user_id})
    logger.info(f"User {user_id} removed from AFK")

def is_afk(user_id: int):
    """
    Check if user is AFK.
    Returns None if not AFK, else dict with reason & since.
    """
    return afk_collection.find_one({"user_id": user_id})

