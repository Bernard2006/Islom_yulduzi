from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from keyboards.inline.poklanish import *
from keyboards.inline.erkak_bomdod import *
from aiogram.types import CallbackQuery, InputFile


@dp.message_handler(text='🔗Poklanish')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(text="Tahorat olish tartibi", reply_markup=poklanish)


@dp.callback_query_handler(text='niyat')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/poklanish/niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"1.<b>Niyat</b> Tahorat olish uchun, iloji bo'lsa, qiblaga yuzlaniladi. "
                                 f"«A'uzu billahi minash-shaytonir rojiym. Bismillahir rohmanir rohiym,"
                                 f" tahorat olmoqlikka niyat qildim», deb niyat qilinadi\n\n.Eslatma: Tirnoqlarga"
                                 f" surilgan lak, teridagi har xil bo'yoqlar ketkazilmasdan olingan tahorat "
                                 f"sahih (haqiqiy) hisoblanmaydi.\n\nTahorat olayotganda gapirmaslik, ehtiyojdan "
                                 f"ortiq suv ishlatmaslik, ust-boshga suv sachratmaslik kerak",
                         reply_markup=bomdod_davomi1)


@dp.callback_query_handler(text='qol')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/poklanish/qollarni_yuvish.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"<b>2. Qo'llarni yuvish</b> \n\nQo'llar bandigacha uch marta yuviladi. Barmoqda uzuk"
                                 f" bo'lsa, qimirlatib, ostiga suv yugurtiriladi. Barmoqlar bir birining "
                                 f"orasiga kiritiladi.",
                         reply_markup=bomdod_davomi2)


@dp.callback_query_handler(text='ogiz')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/poklanish/ogiz_chayqash.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"<b>3. Og'iz chayish </b>\n\n Tishlar misvok yoki tish yuvish pastasi bilan, yoki "
                                 f"qo'l bilan ishqalab yuviladi. O'ng qo'lda suv olinib, og'iz uch marta "
                                 f"g'arg'ara qilib chayiladi",
                         reply_markup=bomdod_davomi3)


@dp.callback_query_handler(text='burun')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/poklanish/burunni_chayish.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"<b>4. Burunni chayish </b> \n\nBurunga o'ng qo'l bilan uch marta suv tortilib, chap qo'l "
                                 f"bilan qoqib tozalanadi",
                         reply_markup=bomdod_davomi4)


@dp.callback_query_handler(text='yuz')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/poklanish/yuzni_yuvish.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"<b>5. Yuzni yuvish</b>\n\n Yuz uch marta yuviladi. Yuzning chegarasi uzunasiga soch "
                                 f"chiqqan joydan jag'ning ostigacha kengligi esa ikki quloq yumshog'ining "
                                 f"orasigacha bo'lgan o'rindir",
                         reply_markup=bomdod_davomi5)


@dp.callback_query_handler(text='qol_tirsak')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/poklanish/qollarni_tirsakkacha_yuvish.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"<b>6. Qo'llarni tirsakgacha yuvish</b>\n\n Avval o'ng qo'l, keyin esa chap qo'l "
                                 f"tirsak bilan qo'shib yuviladi",
                         reply_markup=bomdod_davomi6)


@dp.callback_query_handler(text='bosh_mash')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio="photos/poklanish/boshga_mas'h.jpg")

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"<b>7. Boshga mas'h tortish</b>\n\n Hovuchga suv olib, to'kib tashlab, - ho'li bilan "
                                 f"boshning hamma qismiga bir marta mas'h tortiladi",
                         reply_markup=bomdod_davomi7)


@dp.callback_query_handler(text='quloq_mash')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio="photos/poklanish/quloq_va_bo'yin.jpg")

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"<b>8. Quloq va bo'yinga mas'h tortish</b> \n\n Ko'rsatkich barmoq bilan quloq ichiga "
                                 f"mas'h tortib, bosh barmoq bilan esa quloq orqasi mas'h qilinadi.\n\n Ikkala "
                                 f"kaftning orqasi bilan bo'yin mas'h qilinadi",
                         reply_markup=bomdod_davomi8)


@dp.callback_query_handler(text='oyoq')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/poklanish/oyoqlarni_yuvish.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"<b>9. Oyoqlarni yuvish </b>\n\nChap qo'l bilan o'ng oyoqni oshiq(to'piq) bilan va "
                                 f"barmoqlar orasini(ishqalab) uch marta yuviladi.\n\n Chap oyoq ham shu tarzda uch "
                                 f"marta yuviladi",
                         )
