from pyrogram import filters
from pyrogram.types import CallbackQuery
from Shadow import app
from Shadow.utils.inline.start import details_buttons, credit_buttons

VIDEO_LINK = "https://files.catbox.moe/issfxd.mp4"
CAPTION = "✨💫 𝙎𝙚𝙡𝙚𝙘𝙩 𝙩𝙝𝙚 𝙨𝙚𝙘𝙩𝙞𝙤𝙣 𝙩𝙝𝙖𝙩 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙤𝙥𝙚𝙣 💫✨"

# Show video + Help + Credit buttons
@app.on_callback_query(filters.regex("show_details"))
async def show_details(client, query: CallbackQuery):
    try:
        await query.message.delete()
    except:
        pass

    await client.send_video(
        chat_id=query.message.chat.id,
        video=VIDEO_LINK,
        caption=CAPTION,
        reply_markup=details_buttons()
    )


# Both help and credit buttons send same video + caption
@app.on_callback_query(filters.regex("show_help_video|show_credits_video"))
async def show_help_or_credits(client, query: CallbackQuery):
    await query.answer()  # just to prevent "loading" forever
    try:
        await query.message.delete()
    except:
        pass

    await client.send_video(
        chat_id=query.message.chat.id,
        video=VIDEO_LINK,
        caption=CAPTION,
        reply_markup=credit_buttons()
    )
