#(©)cybermusicproject

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Tentang Bot Ini:\n@newviralkanbot Adalah Bot Telegram Untuk Menyimpan Postingan Atau File Yang Dapat Diakses Melalui Link Khusus.\n\n○ Creator : <a href='tg://user?id={OWNER_ID}'>klik disini</a>\n○ Suport by : <a href='@asupanmahasiswivip'>ASUPAN MAHASISWI ID</a>\n○ Join : <a href='@mahasiswiviralid'>MAHASISWI VIRAL ID</a>\n\n○ Endorse & Iklan Contact : <a href='@kgsawtivx'>CONTACT</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
