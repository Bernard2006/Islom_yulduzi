from aiogram.types import CallbackQuery

from loader import dp
from handlers.users.API.nomoz_vaqtlari import GetFajr,GetIsha,GetAsr,GetDhuhr,GetMaghrib,GetData

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
    data = GetData(text)
    await request.message.answer(f"Namoz Vaqtlari 🕋  {text2}\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")

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
    await request.message.answer(f"Namoz Vaqtlari 🕋 {text2}\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")


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
    await request.message.answer(f"Namoz Vaqtlari 🕋 {text2}\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")



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
    await request.message.answer(f"Namoz Vaqtlari 🕋 {text2}\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")


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
    await request.message.answer(f"Namoz Vaqtlari 🕋 {text2}\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")


@dp.callback_query_handler(text='nam')
async def tarjimon(request: CallbackQuery):
    text = 'namangan'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    await request.message.answer(f"Namoz Vaqtlari 🕋 Namangan\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")


@dp.callback_query_handler(text='nav')
async def tarjimon(request: CallbackQuery):
    text = 'navoi'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    await request.message.answer(f"Namoz Vaqtlari 🕋 Navoi \n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")


@dp.callback_query_handler(text='qash')
async def tarjimon(request: CallbackQuery):
    text = 'qarshi'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    await request.message.answer(f"Namoz Vaqtlari 🕋 Qashqadaryo\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")


@dp.callback_query_handler(text='sama')
async def tarjimon(request: CallbackQuery):
    text = 'samarkand'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    await request.message.answer(f"Namoz Vaqtlari 🕋 Samarqand\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")


@dp.callback_query_handler(text='sir')
async def tarjimon(request: CallbackQuery):
    text = 'gulistan'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    await request.message.answer(f"Namoz Vaqtlari 🕋 Sirdaryo\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")



@dp.callback_query_handler(text='sur')
async def tarjimon(request: CallbackQuery):
    text = 'termez'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    await request.message.answer(f"Namoz Vaqtlari 🕋 Surxondaryo\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")

@dp.callback_query_handler(text='tosh')
async def tarjimon(request: CallbackQuery):
    text = 'tashkent'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    await request.message.answer(f"Namoz Vaqtlari 🕋 Toshkent\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")

@dp.callback_query_handler(text='qora')
async def tarjimon(request: CallbackQuery):
    text = 'nukus'
    lookup = GetFajr(text)
    lookup2 = GetDhuhr(text)
    lookup3 = GetAsr(text)
    lookup4 = GetMaghrib(text)
    lookup5 = GetIsha(text)
    data = GetData(text)
    await request.message.answer(f"Namoz Vaqtlari 🕋 Qoraqalpog'iston\n"
                                 f"\n"
                                 f"<b>Bomdod</b> : {lookup} \n"
                                 f"<b>Peshin</b> : {lookup2} \n"
                                 f"<b>Asr</b> : {lookup3} \n"
                                 f"<b>Shom</b> : {lookup4} \n"
                                 f"<b>Xufton</b> : {lookup5} \n"
                                 f"\n"
                                 f"<b>Yangilanagan sana</b>:  {data}")
