from loader import dp
from aiogram import types
from aiogram.types import CallbackQuery, message
from keyboards.inline.viloyatlar import telefonalr_button


@dp.message_handler(text='⏰Namoz vaqtlari')
async def bot_start(message: types.Message):
    await message.answer(text="<b>O'zingizga kerakli viloyatni tanlang👇</b>", reply_markup=telefonalr_button)