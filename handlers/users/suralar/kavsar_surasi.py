#from keyboards.default.suralar import telefonlar_button
from aiogram import types
from handlers.users.API.kavsar_api import *
from keyboards.inline.kavsar_sura import *
from aiogram.types import CallbackQuery
from handlers.users.API.kavsar_audio import *

from loader import dp

@dp.message_handler(text='🟢Kavsar surasi')
async def tarjimon(message: types.Message):
    look = getKavsar()
    audio2 = getFalaq_audio()
    await message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davom)
@dp.callback_query_handler(text='kavsar_davom')
async def tarjimon(request: CallbackQuery):
    look = getKavsar1()
    audio2 = getFalaq_audio1()
    await request.message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davomi1)
@dp.callback_query_handler(text='kavsar_davom1')
async def tarjimon(request: CallbackQuery):
    look = getKavsar2()
    audio2 = getFalaq_audio2()
    await request.message.answer(f"{look}\n"
                         f"{audio2}", reply_markup=davomi2)
