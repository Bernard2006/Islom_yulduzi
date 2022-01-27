from aiogram import types
from handlers.users.suralar_arab.arab_suralar import *
from loader import dp


@dp.message_handler(commands='Fotiha_surasi')
async def bot_start(message: types.Message):
    fotiha = Fotiha()
    await message.reply(f"<b>Fotiha surasi</b> \n\n{fotiha}")


@dp.message_handler(commands='Sano_duosi')
async def bot_start(message: types.Message):
    sano = Sano_duosi()
    await message.reply(f"<b>Sano duosi</b> \n\n{sano}")


@dp.message_handler(commands='Kavsar')
async def bot_start(message: types.Message):
    kavsar = Kavsar()
    await message.reply(f"<b>Kavsar surasi</b> \n\n{kavsar}")


@dp.message_handler(commands='Ixlos')
async def bot_start(message: types.Message):
    ixlos = Ixlos()
    await message.reply(f"<b>Ixlos surasi</b> \n\n {ixlos}")


@dp.message_handler(commands='Falaq')
async def bot_start(message: types.Message):
    falaq = Falaq()
    await message.reply(f"<b>Falaq surasi</b>\n\n{falaq}")


@dp.message_handler(commands='An_nos')
async def bot_start(message: types.Message):
    an_nos = An_nos()
    await message.reply(f"<b>An_nos surasi</b>\n\n{an_nos}")
