from aiogram.types import  InlineKeyboardButton,InlineKeyboardMarkup

telefonalr_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=' 🕌Andijon',callback_data='and'),
            InlineKeyboardButton(text=" 🕌Buxoro",callback_data='bux')

        ],
        [
            InlineKeyboardButton(text=" 🕌Farg'ona",callback_data='farg'),
            InlineKeyboardButton(text=" 🕌Jizzax",callback_data='jiz')
        ],
        [
            InlineKeyboardButton(text=" 🕌Xorazm",callback_data='xor'),
            InlineKeyboardButton(text=" 🕌Namangan",callback_data='nam')
        ],
        [
            InlineKeyboardButton(text=" 🕌Navoiy",callback_data='nav'),
            InlineKeyboardButton(text=" 🕌Qashqadaryo",callback_data='qash')
        ],
        [
            InlineKeyboardButton(text=" 🕌Samarqand",callback_data='sama'),
            InlineKeyboardButton(text=" 🕌Sirdaryo",callback_data='sir')
        ],
        [
            InlineKeyboardButton(text=" 🕌Surxondaryo",callback_data='sur'),
            InlineKeyboardButton(text=" 🕌Toshkent",callback_data='tosh')
        ],
        [
            InlineKeyboardButton(text=" 🕌Nukus",callback_data='qora')
        ]
    ]
)