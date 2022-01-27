from aiogram import types
from handlers.users.start import bot_start
from loader import dp
from keyboards.default.suralar import suralar_button
from keyboards.default.asosiy_button import telefonlar_button


# Echo bot
@dp.message_handler(text = 'Ortga Qaytish🔙')
async def bot_echo(message: types.Message):
    await message.answer(text="Ortga",reply_markup=suralar_button)


@dp.message_handler(text = 'Menuga qaytish🔙')
async def bot_echo(message: types.Message):
    await message.reply(text="Menu:",reply_markup=telefonlar_button)