from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

poklanish = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='1.Niyat'),
            KeyboardButton(text="2.Qo'llarni yuvish")
        ],
        [
            KeyboardButton(text="3.O'gizni chayqash")
        ],
        [
            KeyboardButton(text="4.Burunni chayish"),
            KeyboardButton(text="5.Yuzni yuvish")
        ],
        [
            KeyboardButton(text="6.Qo'llarni tirsakkacha yuvish"),
        ],
        [
            KeyboardButton(text="7.Boshga mas'h tortish"),
            KeyboardButton(text="8.Quloq va Bo'yinga mas'h tortish"),
        ],
        [
            KeyboardButton(text="9.Oyoqlarni yuvish")
        ],
        [
            KeyboardButton(text="Menuga qaytish🔙")
        ]
    ]
)
