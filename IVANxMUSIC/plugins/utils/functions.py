from datetime import datetime, timedelta
from re import findall
from re import sub as re_sub

from pyrogram import errors
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message

MARKDOWN = """
ʀᴇᴀᴅ ᴛʜᴇ ʙᴇʟᴏᴡ ᴛᴇxᴛ ᴄᴀʀᴇғᴜʟʟʏ ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ʜᴏᴡ ғᴏʀᴍᴀᴛᴛɪɴɢ ᴡᴏʀᴋs!

<u>sᴜᴘᴘᴏʀᴛᴇᴅ ғɪʟʟɪɴɢs:</u>
