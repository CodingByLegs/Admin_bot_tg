from aiogram.types import CallbackQuery

from keyboards.inline.InlineKeyBoard import refresh_categories_kb

from loader import bot, dp
from keyboards.inline.callback_dates import page_callback, refresh_things_kb, thing_page_callback
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline import InlineKeyBoard
from aiogram.dispatcher.filters import Command


@dp.callback_query_handler(page_callback.filter(rotation="forward"))
async def show_next_channels_page(call: CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page_number")) + 1
    await call.message.edit_reply_markup(reply_markup=await refresh_categories_kb(page))


@dp.callback_query_handler(page_callback.filter(rotation="backward"))
async def show_previous_channels_page(call: CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page_number")) - 1
    await call.message.edit_reply_markup(reply_markup=await refresh_categories_kb(page))


@dp.callback_query_handler(thing_page_callback.filter(thing_rotation="forward"))
async def show_next_channels_page(call: CallbackQuery, callback_data: dict):
    page = int(callback_data.get("thing_page_number")) + 1
    await call.message.edit_reply_markup(reply_markup=await refresh_things_kb(page))


@dp.callback_query_handler(thing_page_callback.filter(thing_rotation="backward"))
async def show_previous_channels_page(call: CallbackQuery, callback_data: dict):
    page = int(callback_data.get("thing_page_number")) - 1
    await call.message.edit_reply_markup(reply_markup=await refresh_things_kb(page))
