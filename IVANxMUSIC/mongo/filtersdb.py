# filtersdb.py
from misc import db, logger

filters_col = db["filters"]

def add_filter(chat_id: int, keyword: str, reply: str, type_: str = "text"):
    """
    Add or update a custom filter in a chat.
    """
    filters_col.update_one(
        {"chat_id": chat_id, "keyword": keyword.lower()},
        {"$set": {"reply": reply, "type": type_}},
        upsert=True
    )
    logger.info(f"Added/updated filter '{keyword}' in chat {chat_id}")

def remove_filter(chat_id: int, keyword: str):
    """
    Remove a filter by keyword.
    """
    filters_col.delete_one({"chat_id": chat_id, "keyword": keyword.lower()})
    logger.info(f"Removed filter '{keyword}' from chat {chat_id}")

def get_filter(chat_id: int, keyword: str):
    """
    Get a single filter.
    """
    return filters_col.find_one({"chat_id": chat_id, "keyword": keyword.lower()})

def get_all_filters(chat_id: int):
    """
    Get all filters in a chat.
    """
    return list(filters_col.find({"chat_id": chat_id}))
