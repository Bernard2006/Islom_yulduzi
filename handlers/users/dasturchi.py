from aiogram import types
# from handlers.users.start import bot_start
from loader import dp


# Echo bot
@dp.message_handler(text="💻 Programmer")
async def bot_echo(message: types.Message):
    await message.answer(text="💻 Programmer \n \n T.me: @Not_alone_06 \n \n instagram: "
                              "https://instagram.com/homidovbobur907 \n \n Tel: +998 90 630 77 92")
