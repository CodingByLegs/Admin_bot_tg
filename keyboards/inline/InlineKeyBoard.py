from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from keyboards.inline.callback_dates import category_callback



async def create_categories_kb():
    list_of_categories = ['K', 'd']
    list_of_categories_kb = InlineKeyboardMarkup(row_width=1)
    count_of_categories = 0
    if list_of_categories is not None:
        for category in list_of_categories:
            count_of_categories += 1
            # создаем кнопки с названием каналов и сразу добавляем их в клавиатуру
            inline_button = InlineKeyboardButton(text=category, callback_data="none")
            list_of_categories_kb.insert(inline_button)
            if count_of_categories == 8:  # не более 8 каналов на одной странице
                break
        button_pages1 = InlineKeyboardButton(text="⏺️ ", callback_data="none")
        button_pages2 = InlineKeyboardButton(text=1, callback_data="none")
        if len(list_of_categories) > 8:
            button_pages3 = InlineKeyboardButton(text="➡️")
        else:
            button_pages3 = InlineKeyboardButton(text="⏺️", callback_data="none")
        list_of_categories_kb.row(button_pages1, button_pages2, button_pages3)
    return list_of_categories_kb

