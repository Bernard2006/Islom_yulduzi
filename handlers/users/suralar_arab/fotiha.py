from aiogram.types import CallbackQuery

from keyboards.default.suralar_arab import suralar_button
from aiogram import types
from handlers.users.suralar_arab.arab_suralar import *

from loader import dp


# Echo bot

@dp.callback_query_handler(text='sura')
async def bot_start(request: CallbackQuery):
    await request.message.answer(text='<b>Suralar.Tanlang</b>', reply_markup=suralar_button)
    await request.message.delete()


@dp.message_handler(text='Fotiha')
async def bot(message: types.Message):
    look = Fotiha()
    await message.reply(text=f"<b>Fotiha surasi</b>\n{look}")


@dp.message_handler(text='Falaq')
async def bot(message: types.Message):
    look = Falaq()
    await message.reply(text=f"<b>Falaq surasi</b>\n{look}")


@dp.message_handler(text='Kavsar')
async def bot(message: types.Message):
    look = Kavsar()
    await message.reply(text=f"<b>Kavsar surasi</b>\n{look}")


@dp.message_handler(text='Ixlos')
async def bot(message: types.Message):
    look = Ixlos()
    await message.reply(text=f"<b>Ixlos surasi</b>\n{look}")


@dp.message_handler(text='An-nos')
async def bot(message: types.Message):
    look = An_nos()
    await message.reply(text=f"<b>Fotiha surasi</b>\n{look}")
