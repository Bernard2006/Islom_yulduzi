from aiogram.types import  InlineKeyboardButton,InlineKeyboardMarkup

namoz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🕋Suralar',callback_data='sura'),
            InlineKeyboardButton(text='🕋Tarjima Suralar',callback_data='tarjima'),

        ]
    ]
)