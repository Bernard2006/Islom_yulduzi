from loader import dp
from aiogram import types
from aiogram.types import CallbackQuery, message
from keyboards.inline.quron import namoz
from keyboards.default.namoz_default import namoz_vaqtlari
from keyboards.default.ayol_bomdod import namoz_vaqtlari_ayol


@dp.message_handler(text="🕋Quron")
async def bot_start(message: types.Message):
    await message.answer(text='<b>Tanlang: </b>', reply_markup=namoz)