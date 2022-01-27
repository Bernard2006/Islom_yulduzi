from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from data.config import adminlar, kanalar
from states.holatlar import Postlar
from loader import dp, bot
from keyboards.inline.post_inline import confirmation_keyboard, post_callback


@dp.message_handler(Command("yangi_post"))
async def create_post(message: Message):
    await message.answer("")
    await  Postlar.Post_qbul.set()


@dp.message_handler(state=Postlar.Post_qbul)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(malumot=message.text, username=message.from_user)
    await message.answer(f"Postni tekshirihs uchun yuboraymi?",
                         reply_markup=confirmation_keyboard)
    await Postlar.Rad_etish.set()


@dp.callback_query_handler(post_callback.filter(action="post"), state=Postlar.Rad_etish)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("malumot")
        username = data.get("username")
        await state.finish()
        await call.message.edit_reply_markup()
        await call.message.answer("Post adminga yuborildi")
        await bot.send_message(adminlar[0], f"Foydalanuvchi {username} quyidagi postni yubormoqchi:")
        await bot.send_message(adminlar[0], text, parse_mode="HTML", reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action='cancel'), state=Postlar.Rad_etish)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Post rad etildi")


@dp.message_handler(state=Postlar.Rad_etish)
async def post_unknown(message: Message):
    await message.answer("Chop etish yoki rad etishni tanlang")


@dp.callback_query_handler(post_callback.filter(action='post'), user_id=adminlar[0])
async def approve_post(call: CallbackQuery):
    await call.answer("Chop etishga ruxsat berdingiz.", show_alert=True)
    target_chanel = kanalar[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_chanel)


@dp.callback_query_handler(post_callback.filter(action='cancel'), user_id=adminlar[0])
async def decline_post(call: CallbackQuery):
    await call.answer("Post rad etildi", show_alert=True)
    await call.message.edit_reply_markup()
