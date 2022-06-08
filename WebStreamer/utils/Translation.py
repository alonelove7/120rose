# This file is a part of TG-FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
<i>👋 خوش آمدی,</i>{}\n
<i>💥برای استفاده از ربات کافی است فایل خود را ارسال کرده و سپس لینک آن را دریافت کنید.</i>\n
<b>کانال ما @King_network7 </b>\n\n"""

        HELP_TEXT = """
<i>- .....</a></b>"""

        ABOUT_TEXT = """
<b>⚜ نام : NVS Link Generator Bot</b>\n
<b>🔸ورژن : 3.0.3.1</b>\n
<b>🔹کانال : @king_network7 </b>
"""

        stream_msg_text ="""
<i><u>لینک شما ایجاد شد !</u></i>\n
<b>📂 نام فایل :</b> <i>{}</i>\n
<b>📦 سایز فایل  :</b> <i>{}</i>\n
<b>📥 دانلود :</b> <i>{}</i>\n
<b>🖥تماشا :</b> <i>{}</i>\n
 کانال سازنده ربات\n
@king_network7"""

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
        ],
        [InlineKeyboardButton("دونیت", url=f'https://www.payping.ir/d/WiZG')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close'),
        ],
        [InlineKeyboardButton("دونیت", url=f'https://www.payping.ir/d/WiZG')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close'),
        ],
        [InlineKeyboardButton("دونیت", url=f'https://www.payping.ir/d/WiZG')]
        ]
    )
