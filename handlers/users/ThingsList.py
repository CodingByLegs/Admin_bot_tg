from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline import InlineKeyboardThings
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("things"))
async def things_kb(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Список вещей", reply_markup=await InlineKeyboardThings.create_things_kb())