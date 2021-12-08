from aiogram.types import CallbackQuery

from keyboards.inline.edit_inf_inline import refresh_inf_kb
from loader import bot, dp
from keyboards.inline.callback_info import page_callback
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline import edit_inf_inline
from aiogram.dispatcher.filters import Command


@dp.callback_query_handler(page_callback.filter(rotation="forward"))
async def show_next_channels_page(call: CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page_number")) + 1
    await call.message.edit_reply_markup(reply_markup=await refresh_inf_kb(page))


@dp.callback_query_handler(page_callback.filter(rotation="backward"))
async def show_previous_channels_page(call: CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page_number")) - 1
    await call.message.edit_reply_markup(reply_markup=await refresh_inf_kb(page))
