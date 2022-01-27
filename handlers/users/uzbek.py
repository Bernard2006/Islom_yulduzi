from loader import dp,bot
from aiogram import types
from aiogram.types import CallbackQuery, InputFile
from keyboards.default.asosiy_button import telefonlar_button


@dp.callback_query_handler(text='uz')
async def bot_start(request: CallbackQuery):
        await request.message.answer(" Tanlang 👇",reply_markup=telefonlar_button)
