from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from keyboards.inline.callback_info import chr_callback, page_callback

list_of_characteristics = dict.fromkeys(['Price', 'Size', '3', '4', '5', '6', '7', '8', '9', '10'], 1000)


async def create_inf_kb():
    list_of_chr_kb = InlineKeyboardMarkup(row_width=1)
    count_of_chr = 0
    if list_of_characteristics is not None:
        for characteristic in list_of_characteristics:
            count_of_chr += 1
            # создаем кнопки с названием каналов и сразу добавляем их в клавиатуру
            inline_button = InlineKeyboardButton(text=characteristic,
                                                 callback_info=chr_callback.new(characteristic_name=characteristic,
                                                                                page=1))
            list_of_chr_kb.insert(inline_button)
            if count_of_chr == 8:  # не более 8 каналов на одной странице
                break
        button_pages1 = InlineKeyboardButton(text="⏺️ ", callback_info="none")
        button_pages2 = InlineKeyboardButton(text=1, callback_info="none")
        if len(list_of_characteristics) > 8:
            button_pages3 = InlineKeyboardButton(text="➡️",
                                                 callback_info=page_callback.new(page_number=1, rotation="forward"))
        else:
            button_pages3 = InlineKeyboardButton(text="⏺️", callback_info="none")
        list_of_chr_kb.row(button_pages1, button_pages2, button_pages3)
    return list_of_chr_kb


async def refresh_inf_kb(page: int):
    page = int(page)
    global list_of_characteristics
    list_of_characteristics_change = list_of_characteristics[8 * (page - 1)::]  # пропускаем по 8 страниц, которые вывели до этого
    list_categories_kb = InlineKeyboardMarkup(row_width=1)
    count_of_categories = 0
    for characteristic in list_of_characteristics_change:
        count_of_categories += 1
        # создаем кнопки с названием каналов и сразу добавляем их в клавиатуру
        inline_button = InlineKeyboardButton(text=characteristic,
                                             callback_info=chr_callback.new(characteristic_name=characteristic, page=page))
        list_categories_kb.insert(inline_button)
        if count_of_categories == 8:  # не более 8 каналов на одной странице
            break
    if page > 1:
        button_pages1 = InlineKeyboardButton(text="⬅️", callback_info=page_callback.new(page_number=page,
                                                                                        rotation="backward"))
    else:
        button_pages1 = InlineKeyboardButton(text="⏺️", callback_info="none")
    button_pages2 = InlineKeyboardButton(text=page, callback_info="none")
    if len(list_of_characteristics) > 8:
        button_pages3 = InlineKeyboardButton(text="➡️", callback_info=page_callback.new(page_number=page,
                                                                                        rotation="forward"))
    else:
        button_pages3 = InlineKeyboardButton(text="⏺️", callback_info="none")
    list_categories_kb.row(button_pages1, button_pages2, button_pages3)
    return list_categories_kb
