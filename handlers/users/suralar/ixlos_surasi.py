# from keyboards.default.suralar import telefonlar_button
from aiogram import types
from handlers.users.API.ixlos_api import *
from keyboards.inline.ixlos_sura import *
from aiogram.types import CallbackQuery
from handlers.users.API.ixlos_audio import *

from loader import dp


@dp.message_handler(text='Ixlos surasi')
async def tarjimon(message: types.Message):
    look = getIxlos()
    audio2 = Getaudio1()
    await message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davom)


@dp.callback_query_handler(text='davom')
async def tarjimon(message: types.Message):
    look = getIxlos1()
    audio2 = Getaudio2()
    await message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davomi1)


@dp.callback_query_handler(text='davom1')
async def tarjimon(message: types.Message):
    look = getIxlos2()
    audio2 = Getaudio3()
    await message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davomi2)


@dp.callback_query_handler(text='davom2')
async def tarjimon(message: types.Message):
    look = getIxlos3()
    audio2 = Getaudio4()
    await message.answer(f"{look}\n"
                         f"{audio2}")
