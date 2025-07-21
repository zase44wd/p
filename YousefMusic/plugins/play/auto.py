import random
import string
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InputMediaPhoto
from config import START_IMG_URL
import config
from YousefMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app

from YousefMusic.utils.database import get_served_chats

from config import BANNED_USERS, lyrical, YAFA_CHANNEL

from YousefMusic.misc import SUDOERS


MESSAGE = f"""- اقوي بوت ميوزك قنوات و جروبات سرعه وجوده خارقه

وبدون تهنيج او تقطيع او توقف وكمان ان البوت في مميزات جامدة⚡️♥️.

ارفع البوت ادمن فقناتك او جروبك واستمتع بجوده الصوت و السرعه الخياليه للبوت ⚡️♥️

معرف البوت 🎸 [ @{app.username} ]

➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤e 𝘤𝘩𝘢𝘵 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك ⚡", url=f"https://t.me/{app.username}?startgroup=True")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()
        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)
                except Exception:
                    pass
    except Exception:
        pass

@app.on_message(filters.command(["اعلان للبوت"], ""))
async def auto_broadcast_command(client: Client, message: Message):
    await message.reply("تم بدء نشر اعلان للبوت في جميع المجموعات، يرجى عدم تكرار الامر")
    await send_message_to_chats()
    await message.reply("تم الانتهاء من الاعلان في جميع خاص المستخزمين والمجموعات")
