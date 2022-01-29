from aiogram import types
from handlers.users.API.falaq_api import *
from keyboards.inline.falaq_sura import *
from handlers.users.API.falaq_audio import *
from loader import dp


@dp.message_handler(text='🟢Falaq surasi')
async def tarjimon(message: types.Message):
    look = getfalaq1()
    audio2 = getAudio1()
    await message.answer(f"{look}\n"
                         f"{audio2}",reply_markup=davomi1)
@dp.message_handler(text='davom1')
async def tarjimon(message: types.Message):
    look = getfalaq2()
    audio2 = getAudio2()
    await message.answer(f"{look}\n"
                         f"{audio2}",reply_markup=davomi2)
@dp.message_handler(text='davom2')
async def tarjimon(message: types.Message):
    look = getfalaq3()
    audio2 = getAudio3()
    await message.answer(f"{look}\n"
                         f"{audio2}",reply_markup=davomi3)
@dp.message_handler(text='davom3')
async def tarjimon(message: types.Message):
    look = getfalaq4()
    audio2 = getAudio4()
    await message.answer(f"{look}\n"
                         f"{audio2}",reply_markup=davomi4)
@dp.message_handler(text='davom4')
async def tarjimon(message: types.Message):
    look = getfalaq5()
    audio2 = getAudio5()
    await message.answer(f"{look}\n"
                         f"{audio2}")
