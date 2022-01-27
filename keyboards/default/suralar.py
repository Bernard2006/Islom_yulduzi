from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

suralar_button = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Fotiha surasi'),
            KeyboardButton(text='Falaq surasi')
        ],
        [
            KeyboardButton(text='Kavsar surasi'),
            KeyboardButton(text='Ixlos surasi')
        ],
        [
            KeyboardButton(text='An-nos surasi')
        ],
        [
            KeyboardButton(text="Menuga qaytish🔙")
        ]

    ]
)
