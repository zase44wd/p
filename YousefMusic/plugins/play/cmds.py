#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from YousefMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["ميوزك", "• الاوامر •", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/89255574d531671fb2fb5.jpg",
        caption=f"""<b>» مرحبـاً بك عـزيـزي </b> {message.from_user.mention} .\n\n<b>» استخـدم الازرار بالاسفـل ⚡\n» لـ تصفـح اوامـر سورس ماحنيت</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامــر الجروبات •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• اوامـر القناة •", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "• اوامـر الادمـن •", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                       "• اوامــر المطــور •", callback_data="zzzdv"),
                    InlineKeyboardButton(
                        "رجـوع",       callback_data="zzzback"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "حسين", url="https://t.me/XXBTL"),
                ],
            ]
        ),
    )


