# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from WebStreamer import bot_info
from pyrogram.types.messages_and_media import message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


def get_filename(x):
    ex = (
        x.audio or x.animation x.photo or x.sticker \
        or x.voice or x.video_note or x.video or x.document
    )
    if ex:
        return ex.file_name or ""
    return None

@StreamBot.on_message(filters.command(["link", f"link@{bot_info.username}"]))
async def media_receive_handler(_, m: Message):
    rm = m.reply_to_message
    if not (rm and rm.media):
        return
    file_name = get_filename(rm)
    if file_name is None:
        return
    log_msg = await rm.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = Var.URL + 'meta/' + str(log_msg.message_id) + '/' + quote_plus(file_name)
    await rm.reply_text(
        text="`{}`".format(stream_link),
        quote=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🕹️ Click Here to Download 🕹️', url=stream_link)]])
    )
