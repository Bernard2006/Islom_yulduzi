from aiogram import types
from handlers.users.start import bot_start
from loader import dp


# Echo bot
@dp.message_handler(text="ℹ️Ma'lumot")
async def bot_echo(message: types.Message):
    await message.answer(text="Islom Yulduzi🕋 \n\n Bu bot orqali siz: \n"
                              " - ⏰Namoz vaqtlari \n - 🕋Qurondagi kichik suralar \n -🤲Erkaklar yoki Ayollar uchun "
                              "namoz o'qishni o'rganishingiz mumkin \n \n 💻 Dasturchi: @Not_alone_06")