from aiogram.types import  InlineKeyboardButton,InlineKeyboardMarkup

namoz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Erkaklar👱🏻‍♂️',callback_data='erkak'),
            InlineKeyboardButton(text='Ayollar👩🏻‍🦳',callback_data='ayol'),

        ]
    ]
)

