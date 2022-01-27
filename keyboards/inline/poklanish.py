from aiogram.types import  InlineKeyboardButton,InlineKeyboardMarkup

poklanish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1.Niyat',callback_data='niyat'),
            InlineKeyboardButton(text="2. Qo'llarni yuvish",callback_data='qol'),

        ],
        [
            InlineKeyboardButton(text="3. Og'iz chayish", callback_data='ogiz'),
            InlineKeyboardButton(text="4. Burunni chayish", callback_data='burun'),
        ],
        [
            InlineKeyboardButton(text="5. Yuzni yuvish", callback_data='yuz'),
            InlineKeyboardButton(text="6. Qo'llarni tirsakgacha yuvish", callback_data='qol_tirsak'),
        ],
        [
            InlineKeyboardButton(text="7. Boshga mas'h tortish", callback_data='bosh_mash'),
            InlineKeyboardButton(text="8. Quloq va bo'yinga mas'h tortish", callback_data='quloq_mash'),
        ],
        [
            InlineKeyboardButton(text="9. Oyoqlarni yuvish", callback_data='oyoq'),
        ]
    ]
)