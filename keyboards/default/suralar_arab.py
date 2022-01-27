from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

suralar_button = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Fotiha'),
            KeyboardButton(text='Falaq')
        ],
        [
            KeyboardButton(text='Kavsar'),
            KeyboardButton(text='Ixlos')
        ],
        [
            KeyboardButton(text='An-nos')
        ],
        [
            KeyboardButton(text="Menuga qaytish🔙")
        ]

    ]
)
