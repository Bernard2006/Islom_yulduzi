from keyboards.default.suralar import suralar_button
from aiogram import types
from handlers.users.API.fotiha_api import *
from keyboards.inline.fotiha_sura import *
from aiogram.types import CallbackQuery
from handlers.users.API.fotiha_audio import *

from loader import dp


# Echo bot

@dp.callback_query_handler(text='tarjima')
async def bot_start(request: CallbackQuery):
    await request.message.answer(text='<b>Suralar</b> ', reply_markup=suralar_button)
    await request.message.delete()


# Echo bot
@dp.message_handler(text='Fotiha surasi')
async def tarjimon(message: types.Message):
    look = GetFotiha()
    audio2 = Getaudio()
    await message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davom)


@dp.callback_query_handler(text='davom')
async def tarjimon(request: CallbackQuery):
    look = GetFotiha1()
    audio1 = Getaudio1()
    await request.message.answer(f"{look}"
                                 f"{audio1}", reply_markup=davomi1)
@dp.callback_query_handler(text='davom1')
async def tarjimon(request: CallbackQuery):
    look = GetFotiha2()
    audio2 = Getaudio2()
    await request.message.answer(f"{look}"
                                 f"{audio2}", reply_markup=davomi2)

@dp.callback_query_handler(text='davom2')
async def tarjimon(request: CallbackQuery):
    look = GetFotiha3()
    audio2 = Getaudio3()
    await request.message.answer(f"{look}"
                                 f"{audio2}", reply_markup=davomi3)

@dp.callback_query_handler(text='davom3')
async def tarjimon(request: CallbackQuery):
    look = GetFotiha4()
    audio2 = Getaudio4()
    await request.message.answer(f"{look}"
                                 f"{audio2}", reply_markup=davomi4)

@dp.callback_query_handler(text='davom4')
async def tarjimon(request: CallbackQuery):
    look = GetFotiha5()
    audio2 = Getaudio5()
    await request.message.answer(f"{look}"
                                 f"{audio2}", reply_markup=davomi5)

@dp.callback_query_handler(text='davom5')
async def tarjimon(request: CallbackQuery):
    look = GetFotiha6()
    audio2 = Getaudio6()
    await request.message.answer(f"{look}"
                                 f"{audio2}")





