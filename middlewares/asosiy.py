from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import CallbackQuery
from data.config import kanalar
from utils import azolik
from loader import bot, dp

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Asosiy_cheking(BaseMiddleware):
    async def on_pre_process_update(self, xabar: types.Update, data: dict):
        global matn
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        if xabar.message:
            matn = f"Assalomu Alekum {xabar.message.from_user.full_name}!" \
                   f"\n\nBotimizda to'liq foydalanish quyidagi kanalimizga a'zo bo'ling:"

        dastlabki_holati = True

        for k in kanalar:
            holat = await azolik.tekshirish(user_id=user_id, kanal=k)
            dastlabki_holati *= holat

            kanal = await bot.get_chat(k)
            if not holat:
                link = await kanal.export_invite_link()
                telefonalr_button = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text=f'1️⃣ - KANAL', url=f'{link}')
                        ],

                    ]
                )

            if not dastlabki_holati:
                await xabar.message.reply(matn, disable_web_page_preview=True, reply_markup=telefonalr_button)
                raise CancelHandler()
