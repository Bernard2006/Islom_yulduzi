from aiogram.types import CallbackQuery

from loader import dp
from handlers.users.API.nomoz_vaqtlari import *
from keyboards.inline.namoz_vaqt import namoz_vaqt
from datetime import date, time, datetime

today = date.today()
time2 = datetime.now()


# Echo bot
@dp.callback_query_handler(text='farg')
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
    hijriy = GetHijriy(text)
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


@dp.callback_query_handler(text='and')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='bux')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='jiz')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='xor')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='nam')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='nav')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='qash')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='sama')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='sir')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='sur')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='tosh')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()


@dp.callback_query_handler(text='qora')
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
                                 reply_markup=namoz_vaqt)
    await request.message.delete()
