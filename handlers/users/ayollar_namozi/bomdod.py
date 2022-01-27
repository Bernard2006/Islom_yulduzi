from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from keyboards.default.namoz_default import *
from keyboards.inline.ayol_bomdod import *
from aiogram.types import CallbackQuery, InputFile


@dp.message_handler(text='Bomdod namozi ayol')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"1. Niyat\n\n Bomdod namozi ikki rakat sunnat, ikki rakat farz – jami to'rt rakatdan "
                                 f"iborat. \n\nBomdod namozining ikki rakat sunnati quyidagicha o'qiladi:\n\n «Alloh "
                                 f"rizoligi uchun qibla tomonga yuzlanib, bugungi bomdod namozining ikki rakat "
                                 f"sunnatini o'z vaqtida o'qishni niyat qildim», deb ko'ngildan o'tkaziladi ",
                         reply_markup=bomdod_davomi1)


@dp.callback_query_handler(text='ayol_davom1')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_takbir.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="2. Takbir\n\n Iftitoh takbiri: - «Allohu akbar» deb aytilib namozga kiriladi.\n\n"
                                 " Qo'llar yelka barobarida ko'tariladi ", reply_markup=bomdod_davomi2)


@dp.callback_query_handler(text='ayol_davom2')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="3. Qiyom\n\n Qo'llar bog'lanadi. O'ng qo'l chap qo'l ustida tutilib, qo'llar "
                                 "ko'krakka qo'yiladi.\n\n Bu holat «qiyom» deyiladi. Qiyomda (tik turgan holda) "
                                 "sajda qilinadigan joyga qarab, navbati bilan quyidagilar o'qiladi:"
                                 "\n \n /Sano_duosi \n \n /Fotiha_surasi Fotiha surasidan so'ng bir zam "
                                 "(qo'shimcha) sura "
                                 "o'qiladi.\n \n Yangi o'rganuvchilar quyidagi kichik suralardan birini zam "
                                 "qilishsa bo'ladi:"
                                 " \n - /Kavsar \n - /Ixlos \n- /Falaq - /An_nos",
                         reply_markup=bomdod_davomi3)


@dp.callback_query_handler(text='ayol_davom3')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="4. Ruku\n\n Zam sura tugagach, «Allohu akbar», deb ruku qilinadi. Biroz egilinadi."
                                 " Tizzalar bir oz bukiladi. Barmoqlar jamlanib, tizzalarni tutadi.\n\n Rukuda uch"
                                 " marta «Subhana robbiyal 'aziym» (Ey buyuk Robbim, Sen barcha nuqsonlardan"
                                 " poksan), deyiladi", reply_markup=bomdod_davomi4)


@dp.callback_query_handler(text='ayol_davom4')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="5. Qavma\n\n Rukudan «Sami'allohu liman hamidah» (Alloh Uni hamd etganlarni "
                                 "eshitguvchidir), deb qad ko'tariladi, bu holat «qavma» deyiladi.\n\n"
                                 "Qavma holida: «Robbana lakal hamd» (Ey Robbimiz, har turli hamd-sanolar "
                                 "yolg'iz Sengadir), deyiladi", reply_markup=bomdod_davomi5)


@dp.callback_query_handler(text='ayol_davom5')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="6. Sajda\n\n «Allohu akbar» deb avvalo tizzalar, keyin qo'llar va tirsak, "
                                 "so'ng peshona va burun yerga tekkizilib, sajda qilinadi. Sajda qilinayotganda"
                                 " oyoq panjalari qiblaga qaratiladi, tirsaklar yerga tegadi. Sajdada uch marta:"
                                 " «Subhana robbiyal a'la» (Ey ulug' Robbim, Sen butun nuqsonlardan poksan),"
                                 " deyiladi.", reply_markup=bomdod_davomi6)


@dp.callback_query_handler(text='ayol_davom6')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="7. Jalsa \n\n«Allohu akbar» deb sajdadan bosh ko'tariladi va tiz cho'kkan"
                                 " holda bir oz o'tiriladi, bu holat «jalsa» deyiladi. Jalsada qo'llar, "
                                 "barmoqlar o'z holicha tutilib, songa qo'yiladi. \n\nBarmoq uchlari tizza "
                                 "bilan teng bo'lishi lozim. Oyoqlar o'ng tomonga chiqarilib o'tiriladi",
                         reply_markup=bomdod_davomi7)
@dp.callback_query_handler(text='ayol_davom7')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="8. Sajda \n\n«Allohu akbar», deb ikkinchi marta sajda qilinadi. "
                                 "Sajdada uch marta: «Subhana robbiyal a'la», deyiladi. "
                                 "Shu bilan birinchi rakat tugaydi.",
                         reply_markup=bomdod_davomi8)
@dp.callback_query_handler(text='ayol_davom8')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="9. 2-chi rakat. Qiyom\n\n «Allohu akbar», deb qiyomga (tikka) turiladi. "
                                 "Qiyomda «Bismillahir rohmanir rohiym»dan boshlab, Fotiha surasi, "
                                 "orqasidan bir zam sura o'qiladi",
                         reply_markup=bomdod_davomi9)
@dp.callback_query_handler(text='ayol_davom9')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="10. Ruku \n\n«Allohu akbar», deb ruku qilinadi. Rukuda uch marta «Subhana "
                                 "robbiyal 'aziym» , deyiladi",
                         reply_markup=bomdod_davomi10)
@dp.callback_query_handler(text='ayol_davom10')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="11. Qavma \n\n«Sami'allohu liman hamidah», deb tik turiladi, ketidan "
                                 "«Robbana lakal hamd», deyiladi ",
                         reply_markup=bomdod_davomi11)
@dp.callback_query_handler(text='ayol_davom11')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="12. Sajda\n\n «Allohu akbar», deb sajdaga boriladi. Sajdada uch marta "
                                 "«Subhana robbiyal a'la» , deyiladi",
                         reply_markup=bomdod_davomi12)
@dp.callback_query_handler(text='ayol_davom12')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="13. Jalsa \n\n«Allohu akbar», deb sajdadan bosh ko'tariladi va bir oz o'tiriladi",
                         reply_markup=bomdod_davomi13)
@dp.callback_query_handler(text='ayol_davom13')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="14. Sajda \n\n«Allohu akbar», deb ikkinchi marta sajda qilinadi. "
                                 "Sajdada uch marta: «Subhana robbiyal a'la» , deyiladi",
                         reply_markup=bomdod_davomi14)
@dp.callback_query_handler(text='ayol_davom14')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="15. Qa'da \n\n «Allohu akbar», deb sajdadan bosh ko'tarilibqa'dada "
                                 "o'tiriladi va quyidagilar o'qiladi:",
                         reply_markup=bomdod_davomi15)


@dp.callback_query_handler(text='ayol_davom15')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_salom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="16. Salom\n\n Avval o'ng, keyin chap yelkaga qarab: «Assalamu "
                                 "alaykum va rohmatulloh» deb salom berilib namozdan chiqiladi",
                         reply_markup=bomdod_davomi16)
@dp.callback_query_handler(text='ayol_davom16')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_salom.jpg')

    await bot.send_photo(chat_id=user_id,
                         caption="Yakun \n\nShu bilan bomdod namozining ikki rakat sunnati tugaydi.\n\n "
                                 "Bomdod namozining ikki rakat farzi ham xuddi shu tartibda o'qiladi.\n\n"
                                 " Bomdod namozining farziga quyidagicha niyat qilinadi: «Alloh rizoligi "
                                 "uchun bomdod namozining ikki rakat farzini o'z vaqtida o'qishni niyat qildim»."
                                 " Qolgan qismi sunnat bilan bir xil davom etaveradi.")

