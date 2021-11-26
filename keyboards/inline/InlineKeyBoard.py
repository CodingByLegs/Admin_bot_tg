from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from keyboards.inline.callback_dates import category_callback, page_callback


list_of_categories = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']


async def create_categories_kb():
    list_of_categories_kb = InlineKeyboardMarkup(row_width=1)
    count_of_categories = 0
    if list_of_categories is not None:
        for category in list_of_categories:
            count_of_categories += 1
            # создаем кнопки с названием каналов и сразу добавляем их в клавиатуру
            inline_button = InlineKeyboardButton(text=category, callback_data=category_callback.new(category_name=category, page=1))
            list_of_categories_kb.insert(inline_button)
            if count_of_categories == 8:  # не более 8 каналов на одной странице
                break
        button_pages1 = InlineKeyboardButton(text="⏺️ ", callback_data="none")
        button_pages2 = InlineKeyboardButton(text=1, callback_data="none")
        if len(list_of_categories) > 8:
            button_pages3 = InlineKeyboardButton(text="➡️", callback_data=page_callback.new(page_number=1, rotation="forward"))
        else:
            button_pages3 = InlineKeyboardButton(text="⏺️", callback_data="none")
        list_of_categories_kb.row(button_pages1, button_pages2, button_pages3)
    return list_of_categories_kb


async def refresh_categories_kb(page: int):
    page = int(page)
    global list_of_categories
    list_of_categories_change = list_of_categories[8 * (page - 1)::]  # пропускаем по 8 страниц, которые вывели до этого
    list_categories_kb = InlineKeyboardMarkup(row_width=1)
    count_of_categories = 0
    for category in list_of_categories_change:
        count_of_categories += 1
        # создаем кнопки с названием каналов и сразу добавляем их в клавиатуру
        inline_button = InlineKeyboardButton(text=category,
                                             callback_data=category_callback.new(category_name=category, page=page))
        list_categories_kb.insert(inline_button)
        if count_of_categories == 8:  # не более 8 каналов на одной странице
            break
    if page > 1:
        button_pages1 = InlineKeyboardButton(text="⬅️", callback_data=page_callback.new(page_number=page,
                                                                                        rotation="backward"))
    else:
        button_pages1 = InlineKeyboardButton(text="⏺️", callback_data="none")
    button_pages2 = InlineKeyboardButton(text=page, callback_data="none")
    if len(list_of_categories) > 8:
        button_pages3 = InlineKeyboardButton(text="➡️", callback_data=page_callback.new(page_number=page,
                                                                                        rotation="forward"))
    else:
        button_pages3 = InlineKeyboardButton(text="⏺️", callback_data="none")
    list_categories_kb.row(button_pages1, button_pages2, button_pages3)
    return list_categories_kb