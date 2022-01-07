# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply(f'**Hemlo {m.from_user.mention(style="md")} 😌**

**Send any file to get a shareable link...😌**

__Note: Inappropriate (NSFW) contents will be deleted as soon as it’s noticed 🙂__

**With ❤️ by @MarineBots**',
                  reply_markup=InlineKeyboardMarkup(
                      [[
                            InlineKeyboardButton(
                                  f'{emoji.STAR} Source {emoji.STAR}',
                                  url='https://github.com/EverythingSuckz/TG-FileStreamBot')
                        ]]
                  ))
