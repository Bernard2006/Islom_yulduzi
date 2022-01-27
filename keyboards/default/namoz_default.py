from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

namoz_vaqtlari = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Bomdod namozi'),
            KeyboardButton(text='Asr namozi')
        ],
        [
            KeyboardButton(text='Peshin namozi')
        ],
        [
            KeyboardButton(text="Shom namozi"),
            KeyboardButton(text="Xufton namozi")
        ],
        [
            KeyboardButton(text="Menuga qaytish🔙")
        ]
    ]
)
