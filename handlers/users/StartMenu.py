from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline import InlineKeyBoard
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("start"))
async def categories_kb(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Категории товаров", reply_markup=await InlineKeyBoard.create_categories_kb())
