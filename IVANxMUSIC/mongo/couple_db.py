# couple_db.py
from misc import db, logger
from datetime import datetime

couples = db["couples"]

def make_couple(user_id: int, partner_id: int):
    """
    Create a couple. Will remove previous couple if exists.
    """
    remove_couple(user_id)
    remove_couple(partner_id)
    couples.insert_one({
        "user_id": user_id,
        "partner_id": partner_id,
        "since": datetime.utcnow()
    })
    couples.insert_one({
        "user_id": partner_id,
        "partner_id": user_id,
        "since": datetime.utcnow()
    })
    logger.info(f"Couple created: {user_id} ❤️ {partner_id}")

def remove_couple(user_id: int):
    """
    Remove user from couple.
    """
    couples.delete_many({"user_id": user_id})
    logger.info(f"Removed couple for user: {user_id}")

def get_partner(user_id: int):
    """
    Get user's partner. Returns None if single.
    """
    record = couples.find_one({"user_id": user_id})
    if record:
        return record["partner_id"]
    return None

def get_since(user_id: int):
    """
    Get date when the couple was formed.
    """
    record = couples.find_one({"user_id": user_id})
    if record:
        return record["since"]
    return None
