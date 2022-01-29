from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

namoz_vaqtlari_ayol = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='🔹Bomdod namozi ayol'),
            KeyboardButton(text='🔹Asr namozi ayol')
        ],
        [
            KeyboardButton(text='🔹Peshin namozi ayol')
        ],
        [
            KeyboardButton(text="🔹Shom namozi ayol"),
            KeyboardButton(text="🔹Xufton namozi ayol")
        ],
        [
            KeyboardButton(text="Menuga qaytish🔙")
        ]
    ]
)
