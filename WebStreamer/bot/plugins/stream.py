# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from pyrogram.types.messages_and_media import message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.command("link") & filters.private, group=2)
async def media_receive_handler(_, m: Message):
    rm = m.reply_to_message
    if not (rm and rm.media):
        return
    if not (rm.document or rm.video or rm.audio):
        return await rm.reply_text('Invalid Media!', quote=True)
    file_name = ''
    file_name = rm.file_name
    log_msg = await rm.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = Var.URL + str(log_msg.message_id) + '/' +quote_plus(file_name) if file_name else ''
    await rm.reply_text(
        text="`{}`".format(stream_link),
        quote=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🕹️ Click Here to Download 🕹️', url=stream_link)]])
    )
