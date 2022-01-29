from aiogram.types import CallbackQuery

from loader import dp
from handlers.users.API.nomoz_vaqtlari import *
from keyboards.inline.namoz_vaqt import namoz_vaqt
from keyboards.inline.namoz_vaqt import *
from datetime import date, time, datetime

today = date.today()
time2 = datetime.now()


# Echo bot
@dp.callback_query_handler(text='yangilash')
async def tarjimon(request: CallbackQuery):
    text = 'fergana'
    text2 = "Farg'ona"
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash1')
async def tarjimon(request: CallbackQuery):
    text = 'andijan'
    text2 = "Andijon"
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt1)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash2')
async def tarjimon(request: CallbackQuery):
    text = 'bukhara'
    text2 = 'Buxoro'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt2)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash3')
async def tarjimon(request: CallbackQuery):
    text = 'jizzakh'
    text2 = "Jizzax"
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt3)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash4')
async def tarjimon(request: CallbackQuery):
    text = 'urgench'
    text2 = "Xorazm"
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt4)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash5')
async def tarjimon(request: CallbackQuery):
    text = 'namangan'
    text2 = 'Namangan'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt5)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash6')
async def tarjimon(request: CallbackQuery):
    text = 'navoi'
    text2 = 'Navoi'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt6)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash7')
async def tarjimon(request: CallbackQuery):
    text = 'qarshi'
    text2 = "Qashqadaryo"
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt7)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash8')
async def tarjimon(request: CallbackQuery):
    text = 'samarkand'
    text2 = "Samarqand"
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt8)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash9')
async def tarjimon(request: CallbackQuery):
    text = 'gulistan'
    text2 = 'Sirdaryo'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt9)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash10')
async def tarjimon(request: CallbackQuery):
    text = 'termez'
    text2 = "Surxondaryo"
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt10)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash11')
async def tarjimon(request: CallbackQuery):
    text = 'tashkent'
    text2 = "Tashkent"
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt11)
    await request.message.delete()


@dp.callback_query_handler(text='yangilash12')
async def tarjimon(request: CallbackQuery):
    text = 'nukus'
    text2 = 'Nukus'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    lookup6 = GetSunrise(text)
    lookup7 = GetImsak(text)
    data = GetData(text)
    year = time2.year
    month = time2.month
    week = time2.weekday()
    day = time2.day
    hour = time2.hour
    hijriy = GetHijriy(text)

    await request.message.answer(f"Namoz Vaqtlari:\n"
                                 f"=========================\n"
                                 f" 📌 《 🏙 {text2}》 vaqti bilan\n "
                                 f"--------------------------------------------\n "
                                 f"🌓  Tong:         -  {lookup7}\n"
                                 f"  🌞  Quyosh:     -  {lookup6}\n \n"
                                 f"🕰  Bomdod:   -   {lookup}\n"
                                 f"🕰  Peshin:      -  {lookup2} \n"
                                 f"🕰  Asr:           -  {lookup3} \n"
                                 f"🕰  Shom:       -  {lookup4} \n"
                                 f"🕰  Xufton:      -  {lookup5} \n"
                                 f"--------------------------------------------\n\n "
                                 f"📅 : {data}   📅 Hijriy : {hijriy}",
                                 reply_markup=namoz_vaqt12)
    await request.message.delete()
