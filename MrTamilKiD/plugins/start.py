#Copyright 2024-present, Author: MrTamilKiD

from MrTamilKiD.client import Client
from pyrogram import filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(c: Client, m: Message):
    ''' Start Message of the Bot !!'''

    await m.reply_text(text='''<b>🔰 Hello, I am TamilMVAutoRss and Multi-Tasking Bot! 🔰</b>

I can Do Many things, Check Out My Help Section !!

<b>💯 Bot Created By ♥️ @MrTamilKiD_dc4 ♥️
💥 Powered By ⚡️ TamilMv and tamilblasters ⚡️</b>
<i>If you face any kind of Problem/Error or Feature Request, Message to @MrTamilKiD_dc4</i>''',
        quote=True,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("👥 Group", url="https://t.me/TamilMV_New"),
            InlineKeyboardButton("📇 Website", url="https://www.1tamilmv.lol")]
        ])
    )

