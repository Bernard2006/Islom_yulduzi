import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import adminlar
from keyboards.default.asosiy_button import telefonlar_button

from loader import dp,db,bot


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    name = message.from_user.first_name
    try:
        db.add_user(id=message.from_user.id,
                    name = name,langugae ='ru')
    except sqlite3.IntegrityError as err:
        pass
    await message.reply(f"<b>Assalomu alekum</b>, {message.from_user.full_name}!\nBotimizga Xush kelibsiz ☺️",reply_markup=telefonlar_button)
