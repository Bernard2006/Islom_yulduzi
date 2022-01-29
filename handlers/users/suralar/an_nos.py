from aiogram import types
from handlers.users.API.an_nos import *
from keyboards.inline.an_nos import *
from handlers.users.API.an_nos_audio import *
from loader import dp


@dp.message_handler(text='🟢An-nos surasi')
async def tarjimon(message: types.Message):
    look = GetAnnos1()
    audio2 = getAudio1()
    await message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davomi1)


@dp.callback_query_handler(text='davom1')
async def tarjimon(message: types.Message):
    look = GetAnnos2()
    audio2 = getAudio2()
    await message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davomi2)


@dp.callback_query_handler(text='davom2')
async def tarjimon(message: types.Message):
    look = GetAnnos3()
    audio2 = getAudio3()
    await message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davomi3)


@dp.callback_query_handler(text='davom3')
async def tarjimon(message: types.Message):
    look = GetAnnos4()
    audio2 = getAudio4()
    await message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davomi4)


@dp.callback_query_handler(text='davom4')
async def tarjimon(message: types.Message):
    look = GetAnnos5()
    audio2 = getAudio5()
    await message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davomi5)


@dp.callback_query_handler(text='davom5')
async def tarjimon(message: types.Message):
    look = GetAnnos6()
    audio2 = getAudio6()
    await message.answer(f"{look}\n"
                         f"{audio2}")
