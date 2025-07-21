#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

from YousefMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message

from YousefMusic import app
from YousefMusic.core.call import Zelzaly
from YousefMusic.utils.database import is_music_playing, music_on
from YousefMusic.utils.decorators import AdminRightsCheck
from YousefMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(command(["كمل", "كملي"]) & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if " " in message.text:
        return
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    user_mention = message.from_user.mention if message.from_user else "المشـرف"
    await Zelzaly.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(user_mention), reply_markup=close_markup(_)
    )
