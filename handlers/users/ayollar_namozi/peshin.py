from aiogram import types
from loader import dp, bot
from keyboards.inline.ayol_peshin import *
from aiogram.types import CallbackQuery, InputFile


@dp.message_handler(text='🔹Peshin namozi ayol')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"1. Niyat\n\n Peshin namozi to'rt rakat sunnat, to'rt rakat farz va ikki rakat sunnat – jami o'n rakatdan "
                                 f"iborat. \n\nPeshin namozining to'rt rakat sunnati quyidagicha o'qiladi:\n\n «Alloh "
                                 f"rizoligi uchun qibla tomonga yuzlanib, bugungi peshin namozining to'rt rakat "
                                 f"sunnatini o'z vaqtida o'qishni niyat qildim», deb ko'ngildan o'tkaziladi ",
                         reply_markup=bomdod_davomi1)


@dp.callback_query_handler(text='ayol_peshin1')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_takbir.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="2. Takbir\n\n Iftitoh takbiri: - «Allohu akbar» deb aytilib namozga kiriladi.\n\n"
                                 " Qo'llar yelka barobarida ko'tariladi ", reply_markup=bomdod_davomi2)


@dp.callback_query_handler(text='ayol_peshin2')
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


@dp.callback_query_handler(text='ayol_peshin3')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="4. Ruku\n\n Zam sura tugagach, «Allohu akbar», deb ruku qilinadi. Biroz egilinadi."
                                 " Tizzalar bir oz bukiladi. Barmoqlar jamlanib, tizzalarni tutadi.\n\n Rukuda uch"
                                 " marta «Subhana robbiyal 'aziym» (Ey buyuk Robbim, Sen barcha nuqsonlardan"
                                 " poksan), deyiladi", reply_markup=bomdod_davomi4)


@dp.callback_query_handler(text='ayol_peshin4')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="5. Qavma\n\n Rukudan «Sami'allohu liman hamidah» (Alloh Uni hamd etganlarni "
                                 "eshitguvchidir), deb qad ko'tariladi, bu holat «qavma» deyiladi.\n\n"
                                 "Qavma holida: «Robbana lakal hamd» (Ey Robbimiz, har turli hamd-sanolar "
                                 "yolg'iz Sengadir), deyiladi", reply_markup=bomdod_davomi5)


@dp.callback_query_handler(text='ayol_peshin5')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="6. Sajda\n\n «Allohu akbar» deb avvalo tizzalar, keyin qo'llar va tirsak, "
                                 "so'ng peshona va burun yerga tekkizilib, sajda qilinadi. Sajda qilinayotganda"
                                 " oyoq panjalari qiblaga qaratiladi, tirsaklar yerga tegadi. Sajdada uch marta:"
                                 " «Subhana robbiyal a'la» (Ey ulug' Robbim, Sen butun nuqsonlardan poksan),"
                                 " deyiladi.", reply_markup=bomdod_davomi6)


@dp.callback_query_handler(text='ayol_peshin6')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="7. Jalsa \n\n«Allohu akbar» deb sajdadan bosh ko'tariladi va tiz cho'kkan"
                                 " holda bir oz o'tiriladi, bu holat «jalsa» deyiladi. Jalsada qo'llar, "
                                 "barmoqlar o'z holicha tutilib, songa qo'yiladi. \n\nBarmoq uchlari tizza "
                                 "bilan teng bo'lishi lozim. Oyoqlar o'ng tomonga chiqarilib o'tiriladi",
                         reply_markup=bomdod_davomi7)


@dp.callback_query_handler(text='ayol_peshin7')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="8. Sajda \n\n«Allohu akbar», deb ikkinchi marta sajda qilinadi. "
                                 "Sajdada uch marta: «Subhana robbiyal a'la», deyiladi. "
                                 "Shu bilan birinchi rakat tugaydi.",
                         reply_markup=bomdod_davomi8)


@dp.callback_query_handler(text='ayol_peshin8')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="9. 2-chi rakat. Qiyom\n\n «Allohu akbar», deb qiyomga (tikka) turiladi. "
                                 "Qiyomda «Bismillahir rohmanir rohiym»dan boshlab, Fotiha surasi, "
                                 "orqasidan bir zam sura o'qiladi",
                         reply_markup=bomdod_davomi9)


@dp.callback_query_handler(text='ayol_peshin9')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="10. Ruku \n\n«Allohu akbar», deb ruku qilinadi. Rukuda uch marta «Subhana "
                                 "robbiyal 'aziym» , deyiladi",
                         reply_markup=bomdod_davomi10)


@dp.callback_query_handler(text='ayol_peshin10')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="11. Qavma \n\n«Sami'allohu liman hamidah», deb tik turiladi, ketidan "
                                 "«Robbana lakal hamd», deyiladi ",
                         reply_markup=bomdod_davomi11)


@dp.callback_query_handler(text='ayol_peshin11')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="12. Sajda\n\n «Allohu akbar», deb sajdaga boriladi. Sajdada uch marta "
                                 "«Subhana robbiyal a'la» , deyiladi",
                         reply_markup=bomdod_davomi12)


@dp.callback_query_handler(text='ayol_peshin12')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="13. Jalsa \n\n«Allohu akbar», deb sajdadan bosh ko'tariladi va bir oz o'tiriladi",
                         reply_markup=bomdod_davomi13)


@dp.callback_query_handler(text='ayol_peshin13')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="14. Sajda \n\n«Allohu akbar», deb ikkinchi marta sajda qilinadi. "
                                 "Sajdada uch marta: «Subhana robbiyal a'la» , deyiladi",
                         reply_markup=bomdod_davomi14)


@dp.callback_query_handler(text='ayol_peshin14')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="15. Qa'da \n\n «Allohu akbar», deb sajdadan bosh ko'tarilibqa'dada "
                                 "o'tiriladi va quyidagilar o'qiladi:",
                         reply_markup=bomdod_davomi15)


@dp.callback_query_handler(text='ayol_peshin15')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="16. Qiyom\n\n Qo'llar bog'lanadi. O'ng qo'l chap qo'l ustida tutilib, qo'llar "
                                 "ko'krakka qo'yiladi.\n\n Bu holat «qiyom» deyiladi. Qiyomda (tik turgan holda) "
                                 "sajda qilinadigan joyga qarab, navbati bilan quyidagilar o'qiladi:"
                                 "\n \n /Sano_duosi \n \n /Fotiha_surasi Fotiha surasidan so'ng bir zam "
                                 "(qo'shimcha) sura "
                                 "o'qiladi.\n \n Yangi o'rganuvchilar quyidagi kichik suralardan birini zam "
                                 "qilishsa bo'ladi:"
                                 " \n - /Kavsar \n - /Ixlos \n- /Falaq - /An_nos",
                         reply_markup=bomdod_davomi16)


@dp.callback_query_handler(text='ayol_peshin16')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="17. Ruku\n\n Zam sura tugagach, «Allohu akbar», deb ruku qilinadi. Biroz egilinadi."
                                 " Tizzalar bir oz bukiladi. Barmoqlar jamlanib, tizzalarni tutadi.\n\n Rukuda uch"
                                 " marta «Subhana robbiyal 'aziym» (Ey buyuk Robbim, Sen barcha nuqsonlardan"
                                 " poksan), deyiladi", reply_markup=bomdod_davomi17)


@dp.callback_query_handler(text='ayol_peshin17')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="18. Qavma\n\n Rukudan «Sami'allohu liman hamidah» (Alloh Uni hamd etganlarni "
                                 "eshitguvchidir), deb qad ko'tariladi, bu holat «qavma» deyiladi.\n\n"
                                 "Qavma holida: «Robbana lakal hamd» (Ey Robbimiz, har turli hamd-sanolar "
                                 "yolg'iz Sengadir), deyiladi", reply_markup=bomdod_davomi18)


@dp.callback_query_handler(text='ayol_peshin18')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="19. Sajda\n\n «Allohu akbar» deb avvalo tizzalar, keyin qo'llar va tirsak, "
                                 "so'ng peshona va burun yerga tekkizilib, sajda qilinadi. Sajda qilinayotganda"
                                 " oyoq panjalari qiblaga qaratiladi, tirsaklar yerga tegadi. Sajdada uch marta:"
                                 " «Subhana robbiyal a'la» (Ey ulug' Robbim, Sen butun nuqsonlardan poksan),"
                                 " deyiladi.", reply_markup=bomdod_davomi19)


@dp.callback_query_handler(text='ayol_peshin19')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="20. Jalsa \n\n«Allohu akbar» deb sajdadan bosh ko'tariladi va tiz cho'kkan"
                                 " holda bir oz o'tiriladi, bu holat «jalsa» deyiladi. Jalsada qo'llar, "
                                 "barmoqlar o'z holicha tutilib, songa qo'yiladi. \n\nBarmoq uchlari tizza "
                                 "bilan teng bo'lishi lozim. Oyoqlar o'ng tomonga chiqarilib o'tiriladi",
                         reply_markup=bomdod_davomi20)


@dp.callback_query_handler(text='ayol_peshin20')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')
    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="21. Sajda \n\n«Allohu akbar», deb ikkinchi marta sajda qilinadi. "
                                 "Sajdada uch marta: «Subhana robbiyal a'la», deyiladi. "
                                 "Shu bilan birinchi rakat tugaydi.",
                         reply_markup=bomdod_davomi21)


@dp.callback_query_handler(text='ayol_peshin21')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="22. 4-chi rakat. Qiyom\n\n «Allohu akbar», deb qiyomga (tikka) turiladi. "
                                 "Qiyomda «Bismillahir rohmanir rohiym»dan boshlab, Fotiha surasi, "
                                 "orqasidan bir zam sura o'qiladi",
                         reply_markup=bomdod_davomi22)


@dp.callback_query_handler(text='ayol_peshin22')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="23. Ruku \n\n«Allohu akbar», deb ruku qilinadi. Rukuda uch marta «Subhana "
                                 "robbiyal 'aziym» , deyiladi",
                         reply_markup=bomdod_davomi23)


@dp.callback_query_handler(text='ayol_peshin23')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="24. Qavma \n\n«Sami'allohu liman hamidah», deb tik turiladi, ketidan "
                                 "«Robbana lakal hamd», deyiladi ",
                         reply_markup=bomdod_davomi24)


@dp.callback_query_handler(text='ayol_peshin24')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="25. Sajda\n\n «Allohu akbar», deb sajdaga boriladi. Sajdada uch marta "
                                 "«Subhana robbiyal a'la» , deyiladi",
                         reply_markup=bomdod_davomi25)


@dp.callback_query_handler(text='ayol_peshin25')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="26. Jalsa \n\n«Allohu akbar», deb sajdadan bosh ko'tariladi va bir oz o'tiriladi",
                         reply_markup=bomdod_davomi26)


@dp.callback_query_handler(text='ayol_peshin26')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="27. Sajda \n\n«Allohu akbar», deb ikkinchi marta sajda qilinadi. "
                                 "Sajdada uch marta: «Subhana robbiyal a'la» , deyiladi",
                         reply_markup=bomdod_davomi27)


@dp.callback_query_handler(text='ayol_peshin27')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="28. Qa'da \n\n «Allohu akbar», deb sajdadan bosh ko'tarilibqa'dada "
                                 "o'tiriladi va quyidagilar o'qiladi:",
                         reply_markup=bomdod_davomi28)
@dp.callback_query_handler(text='ayol_peshin28')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_salom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="29. Salom\n\n Avval o'ng, keyin chap yelkaga qarab: «Assalamu "
                                 "alaykum va rohmatulloh» deb salom berilib namozdan chiqiladi",
                         reply_markup=bomdod_davomi29)
@dp.callback_query_handler(text='ayol_davom29')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_salom.jpg')

    await bot.send_photo(chat_id=user_id,
                         caption="Yakun\n\n Shu bilan peshin namozining to'rt rakat sunnati tugaydi.\n\n "
                                 "Peshin namozining to'rt rakat farzi ham ayni shu tartibda o'qiladi.\n\n"
                                 " Faqatgina: niyat qilinayotganda «Alloh rizoligi uchun peshin namozining"
                                 " to'rt rakat farzini o'z vaqtida o'qishni niyat qildim» deyiladi va "
                                 "3-4-rakatlarda 'Fotiha' surasidan keyin zam sura qo'shilmaydi..\n\n "
                                 "Peshin namozining ikki rakat sunnati bomdod namozining sunnati kabi "
                                 "o'qiladi. Niyatda «Alloh rizoligi uchun peshin namozining ikki rakat "
                                 "sunnatini o'z vaqtida o'qishni niyat qildim» deb niyat qilinadi")

