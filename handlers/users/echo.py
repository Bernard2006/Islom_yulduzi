from aiogram import types
from handlers.users.start import bot_start
from loader import dp,db


# Echo bot

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
