from aiogram import types
from loader import dp, bot
from keyboards.inline.ayol_asr import *
from aiogram.types import CallbackQuery, InputFile


@dp.message_handler(text='🔹Asr namozi ayol')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption=f"1. Niyat \n \n Asr namozi to'rt rakat farzdan iborat.\n \n Asr namozining "
                                 f"to'rt rakat "
                                 "farzi quyidagicha o'qiladi:\n \n «Alloh rizoligi uchun qibla tomonga yuzlanib, "
                                 "bugungi asr namozining to'rt rakat farz"
                                 " o'z vaqtida o'qishni niyat qildim», "
                                 "deb ko'ngildan o'tkaziladi", reply_markup=asr_davomi1)


@dp.callback_query_handler(text='asr_ayol1')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_takbir.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="2. Takbir \n \n Iftitoh takbiri: - «Allohu akbar» deb aytilib "
                                 "namozga kiriladi", reply_markup=asr_davomi2)


@dp.callback_query_handler(text='asr_ayol2')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="3. Qiyom \n \n  Qiyomda (tik turgan "
                                 "holda)"
                                 " sajda qilinadigan joyga qarab, navbati bilan quyidagilar o'qiladi: "
                                 "\n \n /Sano_duosi \n \n /Fotiha_surasi Fotiha surasidan so'ng bir zam (qo'shimcha) "
                                 "sura "
                                 "o'qiladi.\n \n Yangi o'rganuvchilar quyidagi kichik suralardan birini zam qilishsa "
                                 "bo'ladi:"
                                 " \n - /Kavsar \n - /Ixlos \n- /Falaq - \n/An_nos", reply_markup=asr_davomi3)


@dp.callback_query_handler(text='asr_ayol3')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="4. Ruku\n \n Zam sura tugagach, «Allohu akbar», deb ruku qilinadi. \n \n "
                                 "Rukuda "
                                 "uch marta «Subhana robbiyal 'aziym» (Ey buyuk Robbim, Sen barcha nuqsonlardan "
                                 "poksan), "
                                 "deyiladi", reply_markup=asr_davomi4)


@dp.callback_query_handler(text='asr_ayol4')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="5. Qavma \n \n Rukudan «Sami'allohu liman hamidah» (Alloh Uni hamd etganlarni "
                                 "eshitguvchidir), deb qad ko'tariladi, bu holat «qavma» deyiladi. Qavma holida: "
                                 "«Robbana lakal hamd» (Ey Robbimiz, har turli hamd-sanolar yolg'iz Sengadir), deyiladi"
                         , reply_markup=asr_davomi5)


@dp.callback_query_handler(text='asr_ayol5')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="6. Sajda \n \n «Allohu akbar» Sajdada uch marta: «Subhana robbiyal a'la» "
                                 "(Ey ulug' Robbim, Sen butun nuqsonlardan poksan), deyiladi"
                         , reply_markup=asr_davomi6)


@dp.callback_query_handler(text='asr_ayol6')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="7. Jalsa \n \n «Allohu akbar» deb sajdadan bosh ko'tariladi "
                         , reply_markup=asr_davomi7)


@dp.callback_query_handler(text='asr_ayol7')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="8. Sajda \n \n   «Allohu akbar», deb ikkinchi marta sajda qilinadi. "
                                 "Sajdada uch marta: "
                                 "«Subhana robbiyal a'la», deyiladi. Shu bilan birinchi rakat tugaydi"
                         , reply_markup=asr_davomi8)


@dp.callback_query_handler(text='asr_ayol8')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="9. 2-chi rakat.\n \n Qiyom «Allohu akbar», deb qiyomga (tikka) turiladi. \n \n "
                                 "Qiyomda "
                                 "«Bismillahir rohmanir rohiym»dan boshlab, Fotiha surasi, orqasidan bir zam sura "
                                 "o'qiladi\n \n  /Fotiha_surasi\n \n Zam suralar: \n \n - /Kavsar\n- /Ixlos\n- "
                                 "/Falaq \n - /An_nos "
                         , reply_markup=asr_davomi9)


@dp.callback_query_handler(text='asr_ayol9')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="10. Ruku \n \n «Allohu akbar», deb ruku qilinadi. Rukuda uch marta «Subhana"
                                 " robbiyal 'aziym» , deyiladi"
                         , reply_markup=asr_davomi10)


@dp.callback_query_handler(text='asr_ayol10')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="11. Qavma \n \n «Sami'allohu liman hamidah», deb tik turiladi, ketidan «Robbana "
                                 "lakal hamd», deyiladi"
                         , reply_markup=asr_davomi11)


@dp.callback_query_handler(text='asr_ayol11')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="12. Sajda \n \n«Allohu akbar», deb sajdaga boriladi. Sajdada uch marta"
                                 " «Subhana robbiyal "
                                 "a'la» , deyiladi"
                         , reply_markup=asr_davomi12)


@dp.callback_query_handler(text='asr_ayol12')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="13. Jalsa \n \n«Allohu akbar», deb sajdadan bosh ko'tariladi va bir oz o'tiriladi"
                         , reply_markup=asr_davomi13)


@dp.callback_query_handler(text='asr_ayol13')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="14. Sajda \n \n «Allohu akbar», deb ikkinchi marta sajda qilinadi. Sajdada uch marta:"
                                 " «Subhana robbiyal a'la» , deyiladi"
                         , reply_markup=asr_davomi14)


@dp.callback_query_handler(text='asr_ayol14')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="15. Qa'da \n \n «Allohu akbar», deb sajdadan bosh ko'tarilib qa'dada o'tiriladi va "
                                 "quyidagilar o'qiladi\n \n - /Attahiyyat duosi \n - /Salovat \n- /Duo"
                         , reply_markup=asr_davomi15)


@dp.callback_query_handler(text='asr_ayol15')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="16. 3-chi rakat.\n \n Qiyom «Allohu akbar», deb qiyomga (tikka)"
                                 " turiladi. \n \n Qiyomda "
                                 "«Bismillahir rohmanir rohiym»dan boshlab, Fotiha surasi, orqasidan bir zam sura "
                                 "o'qiladi\n \n  /Fotiha_surasi\n \n Zam suralar: \n \n - /Kavsar\n- /Ixlos\n- "
                                 "/Falaq \n - /An_nos "
                         , reply_markup=asr_davomi16)


@dp.callback_query_handler(text='asr_ayol16')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="17. Ruku \n \n «Allohu akbar», deb ruku qilinadi. Rukuda uch marta «Subhana"
                                 " robbiyal 'aziym» , deyiladi"
                         , reply_markup=asr_davomi17)


@dp.callback_query_handler(text='asr_ayol17')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="18. Qavma \n \n «Sami'allohu liman hamidah», deb tik turiladi, ketidan «Robbana "
                                 "lakal hamd», deyiladi"
                         , reply_markup=asr_davomi18)


@dp.callback_query_handler(text='asr_ayol18')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="19. Sajda \n \n«Allohu akbar», deb sajdaga boriladi. Sajdada uch "
                                 "marta «Subhana robbiyal "
                                 "a'la» , deyiladi"
                         , reply_markup=asr_davomi19)


@dp.callback_query_handler(text='asr_ayol19')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="20. Jalsa \n \n«Allohu akbar», deb sajdadan bosh ko'tariladi va bir oz o'tiriladi"
                         , reply_markup=asr_davomi20)


@dp.callback_query_handler(text='asr_ayol20')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="21. Sajda \n \n «Allohu akbar», deb ikkinchi marta sajda qilinadi. Sajdada uch marta:"
                                 " «Subhana robbiyal a'la» , deyiladi"
                         , reply_markup=asr_davomi21)


@dp.callback_query_handler(text='asr_ayol21')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_qiyom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="22. 4-chi rakat.\n \n Qiyom «Allohu akbar», deb qiyomga (tikka) "
                                 "turiladi. \n \n Qiyomda "
                                 "«Bismillahir rohmanir rohiym»dan boshlab, Fotiha surasi, orqasidan bir zam sura "
                                 "o'qiladi\n \n  /Fotiha_surasi\n \n Zam suralar: \n \n - /Kavsar\n- /Ixlos\n- "
                                 "/Falaq \n - /An_nos "
                         , reply_markup=asr_davomi22)


@dp.callback_query_handler(text='asr_ayol22')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_ruku.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="23. Ruku \n \n «Allohu akbar», deb ruku qilinadi. Rukuda uch marta «Subhana"
                                 " robbiyal 'aziym» , deyiladi"
                         , reply_markup=asr_davomi23)


@dp.callback_query_handler(text='asr_ayol23')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_niyat.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="24. Qavma \n \n «Sami'allohu liman hamidah», deb tik turiladi, ketidan «Robbana "
                                 "lakal hamd», deyiladi"
                         , reply_markup=asr_davomi24)


@dp.callback_query_handler(text='asr_ayol24')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="25. Sajda \n \n«Allohu akbar», deb sajdaga boriladi. Sajdada uch marta "
                                 "«Subhana robbiyal "
                                 "a'la» , deyiladi"
                         , reply_markup=asr_davomi25)


@dp.callback_query_handler(text='asr_ayol25')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="26. Jalsa \n \n«Allohu akbar», deb sajdadan bosh ko'tariladi va bir oz o'tiriladi"
                         , reply_markup=asr_davomi26)


@dp.callback_query_handler(text='asr_ayol26')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_sajda.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="27. Sajda \n \n «Allohu akbar», deb ikkinchi marta sajda qilinadi. Sajdada uch marta:"
                                 " «Subhana robbiyal a'la» , deyiladi"
                         , reply_markup=asr_davomi27)

@dp.callback_query_handler(text='asr_ayol27')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_jalsa.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="28. Qa'da \n \n «Allohu akbar», deb sajdadan bosh ko'tarilib qa'dada o'tiriladi va "
                                 "quyidagilar o'qiladi\n \n - /Attahiyyat duosi \n - /Salovat \n- /Duo"
                         , reply_markup=asr_davomi28)

@dp.callback_query_handler(text='asr_ayol28')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_salom.jpg')

    await bot.send_photo(chat_id=user_id, photo=niyat,
                         caption="29. Salom \n \n Avval o'ng, keyin chap yelkaga qarab: «Assalamu alaykum va "
                                 "rohmatulloh» deb salom berilib namozdan chiqiladi"
                         , reply_markup=asr_davomi29)
@dp.callback_query_handler(text='asr_ayol29')
async def bot_echo(request: CallbackQuery):
    user_id = request.from_user.id
    niyat = InputFile(path_or_bytesio='photos/ayol_salom.jpg')

    await bot.send_photo(chat_id=user_id,
                         caption="Shu bilan Asr namozi tugaydi" )
