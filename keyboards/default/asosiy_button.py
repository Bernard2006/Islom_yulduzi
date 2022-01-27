from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

telefonlar_button = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='⏰Namoz vaqtlari')
        ],
        [
            KeyboardButton(text='🕋Quron'),
            KeyboardButton(text="🤲Men ham namoz o'qiyman ")
        ],
        [
            KeyboardButton(text="💻 Programmer"),
            KeyboardButton(text="ℹ️Ma'lumot")
        ],
        [
            KeyboardButton(text="✍️Izoh")
        ]
    ]
)
