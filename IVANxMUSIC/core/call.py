# call.py
# Made by Ivan

from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from misc import logger

# Initialize PyTgCalls client
pytgcalls = PyTgCalls(Client("musicbot"))

@pytgcalls.on_stream_end()
async def on_stream_end(_, update: Update):
    logger.info(f"Stream ended in chat: {update.chat_id}")
    # You can auto-leave or auto-play next track here

async def start_calls():
    await pytgcalls.start()
    logger.info("PyTgCalls started successfully!")

async def stop_calls():
    await pytgcalls.stop()
    logger.info("PyTgCalls stopped.")
