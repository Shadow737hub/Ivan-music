from pyrogram import Client
from config import Config

app = Client(
    "music_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

@app.on_message()
async def hello(client, message):
    await message.reply("🎵 Hello! I’m alive!")

if __name__ == "__main__":
    app.run()
