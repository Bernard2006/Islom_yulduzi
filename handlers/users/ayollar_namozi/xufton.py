from aiogram import types
from loader import dp, bot
# from keyboards.default.namoz_default import *
from keyboards.inline.ayol_xufton import *
from aiogram.types import CallbackQuery, InputFile


@dp.message_handler(text='Xufton namozi ayol')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"1. Niyat \n \n Xufton namozi to'rt rakat farzdan iborat.\n \n Farz"
                                 f"namozining to'rt rakat "
                                 "sunnati quyidagicha o'qiladi:\n \n «Alloh rizoligi uchun qibla tomonga yuzlanib, "
                                 "bugungi farz namozining to'rt rakat sunnatini o'z vaqtida o'qishni niyat qildim», "
                                 "deb ko'ngildan o'tkaziladi", reply_markup=peshin_davomi1)


@dp.callback_query_handler(text='xufton_ayol1')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_takbir.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="2. Takbir \n \n Iftitoh takbiri: - «Allohu akbar» deb aytilib "
                                 "namozga kiriladi.Qo'llar kaftini qiblaga qaratib, bosh barmoqlarining "
                                 "uchi quloqlarining yumshoq joyiga tekkiziladi", reply_markup=peshin_davomi2)


@dp.callback_query_handler(text='xufton_ayol2')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="3. Qiyom \n \n Qo'llar bog'lanadi. O'ng qo'l kafti chap qo'l ustiga "
                                 "qo'yiladi. O'ng qo'lning bosh va kichik barmoqlari bilan chap qo'l bilagi ushlanadi."
                                 " Qo'llar kindik ostiga qo'yiladi Bu holat «qiyom» deyiladi. Qiyomda "
                                 "(tik turgan holda)"
                                 " sajda qilinadigan joyga qarab, navbati bilan quyidagilar o'qiladi: "
                                 "\n \n /Sano_duosi \n \n /Fotiha_surasi Fotiha surasidan so'ng bir zam (qo'shimcha)"
                                 " sura "
                                 "o'qiladi.\n \n Yangi o'rganuvchilar quyidagi kichik suralardan "
                                 "birini zam qilishsa bo'ladi:"
                                 " \n - /Kavsar \n - /Ixlos \n- /Falaq - /An_nos", reply_markup=peshin_davomi3)


@dp.callback_query_handler(text='xufton_ayol3')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="4. Ruku\n \n Zam sura tugagach, «Allohu akbar», deb ruku qilinadi. Tirsaklar va "
                                 "tizzalarni"
                                 " bukmasdan, barmoqlarni ochgan holda, tizzalarini mahkam changallab "
                                 "egilinadi.\n \n Rukuda "
                                 "uch marta «Subhana robbiyal 'aziym» (Ey buyuk Robbim, Sen barcha "
                                 "nuqsonlardan poksan), "
                                 "deyiladi", reply_markup=peshin_davomi4),


@dp.callback_query_handler(text='xufton_ayol4')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="5. Qavma \n \n Rukudan «Sami'allohu liman hamidah» (Alloh Uni hamd etganlarni "
                                 "eshitguvchidir), deb qad ko'tariladi, bu holat «qavma» deyiladi. Qavma holida: "
                                 "«Robbana lakal hamd» (Ey Robbimiz, har turli hamd-sanolar yolg'iz Sengadir), "
                                 "deyiladi", reply_markup=peshin_davomi5),


@dp.callback_query_handler(text='xufton_ayol5')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="6. Sajda \n \n «Allohu akbar» deb avvalo tizzalar, keyin qo'llar, so'ng "
                                 "peshona va burun "
                                 "yerga tekkizilib, sajda qilinadi. Sajda qilinayotganda oyoq panjalari qiblaga "
                                 "qaratiladi, tirsaklar yerga tegmaydi. Sajdada uch marta: «Subhana robbiyal a'la» "
                                 "(Ey ulug' Robbim, Sen butun nuqsonlardan poksan), deyiladi",
                         reply_markup=peshin_davomi6),


@dp.callback_query_handler(text='xufton_ayol6')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="7. Jalsa \n \n «Allohu akbar» deb sajdadan bosh ko'tariladi va tiz cho'kkan"
                                 " holda bir "
                                 "oz o'tiriladi, bu holat «jalsa» deyiladi. Jalsada qo'llar, barmoqlar o'z holicha "
                                 "tutilib, songa qo'yiladi.\n \n Barmoq uchlari tizza bilan teng bo'lishi lozim. "
                                 "Chap oyoqlar ustiga o'tiriladi, O'ng oyoq panjalari esa qiblaga qaratiladi",
                         reply_markup=peshin_davomi7),


@dp.callback_query_handler(text='xufton_ayol7')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="8. Sajda \n \n   «Allohu akbar», deb ikkinchi marta sajda qilinadi. Sajdada "
                                 "uch marta: "
                                 "«Subhana robbiyal a'la», deyiladi. Shu bilan birinchi rakat tugaydi",
                         reply_markup=peshin_davomi8),


@dp.callback_query_handler(text='xufton_ayol8')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="9. 2-chi rakat.\n \n Qiyom «Allohu akbar», deb qiyomga (tikka) "
                                 "turiladi. \n \n Qiyomda "
                                 "«Bismillahir rohmanir rohiym»dan boshlab, Fotiha surasi, orqasidan bir zam sura "
                                 "o'qiladi\n \n  /Fotiha_surasi\n \n Zam suralar: \n \n - /Kavsar\n- /Ixlos\n- "
                                 "/Falaq \n - /An_nos "
                         , reply_markup=peshin_davomi9),


@dp.callback_query_handler(text='xufton_ayol9')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="10. Ruku \n \n «Allohu akbar», deb ruku qilinadi. Rukuda uch marta «Subhana"
                                 " robbiyal 'aziym» , deyiladi"
                         , reply_markup=peshin_davomi10),


@dp.callback_query_handler(text='xufton_ayol10')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="11. Qavma \n \n «Sami'allohu liman hamidah», deb tik turiladi, ketidan «Robbana "
                                 "lakal hamd», deyiladi"
                         , reply_markup=peshin_davomi11),


@dp.callback_query_handler(text='xufon_ayol11')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="12. Sajda \n \n«Allohu akbar», deb sajdaga boriladi. Sajdada uch marta "
                                 "«Subhana robbiyal "
                                 "a'la» , deyiladi"
                         , reply_markup=peshin_davomi12),


@dp.callback_query_handler(text='xufon_ayol12')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="13. Jalsa \n \n«Allohu akbar», deb sajdadan bosh ko'tariladi va bir oz o'tiriladi"
                         , reply_markup=peshin_davomi13),


@dp.callback_query_handler(text='xufon_ayol13')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="14. Sajda \n \n «Allohu akbar», deb ikkinchi marta sajda qilinadi. Sajdada uch marta:"
                                 " «Subhana robbiyal a'la» , deyiladi"
                         , reply_markup=peshin_davomi14),


@dp.callback_query_handler(text='xufon_ayol14')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="15. Qa'da \n \n «Allohu akbar», deb sajdadan bosh ko'tarilib qa'dada o'tiriladi va "
                                 "quyidagilar o'qiladi\n \n - /Attahiyyat duosi \n - /Salovat \n- /Duo"
                         , reply_markup=peshin_davomi15),


@dp.callback_query_handler(text='xufon_ayol15')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="16. 3-chi rakat.\n \n Qiyom «Allohu akbar», deb qiyomga (tikka)"
                                 " turiladi. \n \n Qiyomda "
                                 "«Bismillahir rohmanir rohiym»dan boshlab, Fotiha surasi, orqasidan bir zam sura "
                                 "o'qiladi\n \n  /Fotiha_surasi\n \n Zam suralar: \n \n - /Kavsar\n- /Ixlos\n- "
                                 "/Falaq \n - /An_nos "
                         , reply_markup=peshin_davomi16),


@dp.callback_query_handler(text='xufton_ayol16')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="17. Ruku \n \n «Allohu akbar», deb ruku qilinadi. Rukuda uch marta «Subhana"
                                 " robbiyal 'aziym» , deyiladi"
                         , reply_markup=peshin_davomi17),


@dp.callback_query_handler(text='xufton_ayol17')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="18. Qavma \n \n «Sami'allohu liman hamidah», deb tik turiladi, ketidan «Robbana "
                                 "lakal hamd», deyiladi"
                         , reply_markup=peshin_davomi18),


@dp.callback_query_handler(text='xufton_ayol18')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="19. Sajda \n \n«Allohu akbar», deb sajdaga boriladi. Sajdada uch marta "
                                 "«Subhana robbiyal "
                                 "a'la» , deyiladi"
                         , reply_markup=peshin_davomi19),


@dp.callback_query_handler(text='xufton_ayol19')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="20. Jalsa \n \n«Allohu akbar», deb sajdadan bosh ko'tariladi va bir oz o'tiriladi"
                         , reply_markup=peshin_davomi20),


@dp.callback_query_handler(text='xufton_ayol20')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="21. Sajda \n \n «Allohu akbar», deb ikkinchi marta sajda qilinadi. Sajdada uch marta:"
                                 " «Subhana robbiyal a'la» , deyiladi"
                         , reply_markup=peshin_davomi21),


@dp.callback_query_handler(text='xufton_ayol21')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="22. 4-chi rakat.\n \n Qiyom «Allohu akbar», deb qiyomga (tikka) "
                                 "turiladi. \n \n Qiyomda "
                                 "«Bismillahir rohmanir rohiym»dan boshlab, Fotiha surasi, orqasidan bir zam sura "
                                 "o'qiladi\n \n  /Fotiha_surasi\n \n Zam suralar: \n \n - /Kavsar\n- /Ixlos\n- "
                                 "/Falaq \n - /An_nos "
                         , reply_markup=peshin_davomi22),


@dp.callback_query_handler(text='xufton_ayol22')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="23. Ruku \n \n «Allohu akbar», deb ruku qilinadi. Rukuda uch marta «Subhana"
                                 " robbiyal 'aziym» , deyiladi"
                         , reply_markup=peshin_davomi23),


@dp.callback_query_handler(text='xufton_ayol23')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="24. Qavma \n \n «Sami'allohu liman hamidah», deb tik turiladi, ketidan «Robbana "
                                 "lakal hamd», deyiladi"
                         , reply_markup=peshin_davomi24),


@dp.callback_query_handler(text='xufton_ayol24')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="25. Sajda \n \n«Allohu akbar», deb sajdaga boriladi. Sajdada uch marta "
                                 "«Subhana robbiyal "
                                 "a'la» , deyiladi"
                         , reply_markup=peshin_davomi25),


@dp.callback_query_handler(text='xufton_ayol25')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="26. Jalsa \n \n«Allohu akbar», deb sajdadan bosh ko'tariladi va bir oz o'tiriladi"
                         , reply_markup=peshin_davomi26),


@dp.callback_query_handler(text='xufton_ayol 26')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="27. Sajda \n \n «Allohu akbar», deb ikkinchi marta sajda qilinadi. Sajdada uch marta:"
                                 " «Subhana robbiyal a'la» , deyiladi",
                         reply_markup=peshin_davomi27),


@dp.callback_query_handler(text='xufton_ayol 27')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="28. Qa'da \n \n «Allohu akbar», deb sajdadan bosh ko'tarilib qa'dada o'tiriladi va "
                                 "quyidagilar o'qiladi\n \n - /Attahiyyat duosi \n - /Salovat \n- /Duo"
                         , reply_markup=peshin_davomi28),


@dp.callback_query_handler(text='xufton_ayol 28')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_salom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="29. Salom \n \n Avval o'ng, keyin chap yelkaga qarab: «Assalamu alaykum va "
                                 "rohmatulloh» deb salom berilib namozdan chiqiladi"
                         , reply_markup=peshin_davomi29),


@dp.callback_query_handler(text='xufton_ayol 29')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_salom.jpg')

    await bot.send_photo(chat_id=user_id,
                         caption="Yakun Shu bilan xufton namozining to'rt rakat farzi tugaydi. Xufton namozining ikki "
                                 "rakat sunnati bomdod namozining ikki rakat sunnati kabi o'qiladi, faqat niyatda: "
                                 "«Alloh rizoligi uchun, bugungi xufton namozining ikki rakat sunnatini o'z vaqtida "
                                 "o'qishni niyat qildim», deb niyat qilinadi.")
