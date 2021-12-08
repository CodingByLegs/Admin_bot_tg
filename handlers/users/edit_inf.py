from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline import edit_inf_inline
from aiogram.dispatcher.filters import Command


@dp.callback_query_handler(func=lambda c: c.data == 'chr1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая характеристика!')


@dp.message_handler(Command("edit_inf"))
async def categories_kb(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "*Товар*", reply_markup=await edit_inf_inline.create_inf_kb())
