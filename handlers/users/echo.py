from aiogram import types
from handlers.users.start import bot_start
from loader import dp,db


# Echo bot
@dp.message_handler(commands='baza')
async def bot(message: types.Message):
    db.create_table_users()
    await message.answer(text='baza yaratildi')
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
