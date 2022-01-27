from loader import dp
from aiogram import types
from aiogram.types import CallbackQuery, message
from keyboards.default.namoz import namoz
from keyboards.default.namoz_default import namoz_vaqtlari
from keyboards.default.ayol_bomdod import namoz_vaqtlari_ayol


@dp.message_handler(text="🤲Men ham namoz o'qiyman")
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang: ', reply_markup=namoz)

@dp.message_handler(text="👱🏻‍♂️Erkaklar")
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang: ', reply_markup=namoz_vaqtlari)
@dp.message_handler(text="👩🏻‍🦳Ayollar")
async def bot_start(message: types.Message):
    await message.reply(text='Tanlang: ', reply_markup=namoz_vaqtlari_ayol)