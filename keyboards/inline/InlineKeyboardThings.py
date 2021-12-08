from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from keyboards.inline.callback_dates import thing_callback, thing_page_callback

list_of_things = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']


async def create_things_kb():
    list_of_things_kb = InlineKeyboardMarkup(row_width=1)
    count_of_things = 0
    if list_of_things is not None:
        # кнопки сверху
        button_pages1 = InlineKeyboardButton(text="⏺️ ", callback_data="none")
        button_pages2 = InlineKeyboardButton(text=1, callback_data="none")
        if len(list_of_things) > 8:
            button_pages3 = InlineKeyboardButton(text="➡️", callback_data=thing_page_callback.new(thing_page_number=1,
                                                                                                  thing_rotation="forward"))
        else:
            button_pages3 = InlineKeyboardButton(text="⏺️", callback_data="none")
        list_of_things_kb.row(button_pages1, button_pages2, button_pages3)
        # товары
        for thing in list_of_things:
            count_of_things += 1
            # создаем кнопки с названием каналов и сразу добавляем их в клавиатуру
            inline_button = InlineKeyboardButton(text=thing,
                                                 callback_data=thing_callback.new(thing_name=thing, thing_page=1))
            list_of_things_kb.insert(inline_button)
            if count_of_things == 8:  # не более 8 каналов на одной странице
                break
        # кнопки снизу
        button_pages4 = InlineKeyboardButton(text="⏺️ ", callback_data="none")
        button_pages5 = InlineKeyboardButton(text="назад", callback_data="none")
        if len(list_of_things) > 8:
            button_pages6 = InlineKeyboardButton(text="➡️", callback_data=thing_page_callback.new(thing_page_number=1,
                                                                                                  thing_rotation="forward"))
        else:
            button_pages6 = InlineKeyboardButton(text="⏺️", callback_data="none")
        list_of_things_kb.row(button_pages4, button_pages5, button_pages6)
    return list_of_things_kb


async def refresh_things_kb(page: int):
    page = int(page)
    global list_of_things
    list_of_things_change = list_of_things[8 * (page - 1)::]  # пропускаем по 8 страниц, которые вывели до этого
    list_things_kb = InlineKeyboardMarkup(row_width=1)
    count_of_things = 0
    #кнопки сверху
    if page > 1:
        button_pages1 = InlineKeyboardButton(text="⬅️", callback_data=thing_page_callback.new(thing_page_number=page,
                                                                                              thing_rotation="backward"))
    else:
        button_pages1 = InlineKeyboardButton(text="⏺️", callback_data="none")
    button_pages2 = InlineKeyboardButton(text=page, callback_data="none")
    if len(list_of_things) > 8:
        button_pages3 = InlineKeyboardButton(text="➡️", callback_data=thing_page_callback.new(thing_page_number=page,
                                                                                              thing_rotation="forward"))
    else:
        button_pages3 = InlineKeyboardButton(text="⏺️", callback_data="none")
    list_things_kb.row(button_pages1, button_pages2, button_pages3)
    #товары
    for thing in list_of_things_change:
        count_of_things += 1
        # создаем кнопки с названием каналов и сразу добавляем их в клавиатуру
        inline_button = InlineKeyboardButton(text=thing,
                                             callback_data=thing_callback.new(thing_name=thing, thing_page=page))
        list_things_kb.insert(inline_button)
        if count_of_things == 8:  # не более 8 каналов на одной странице
            break
    #кнопки снизу
    if page > 1:
        button_pages4 = InlineKeyboardButton(text="⬅️", callback_data=thing_page_callback.new(thing_page_number=page,
                                                                                              thing_rotation="backward"))
    else:
        button_pages4 = InlineKeyboardButton(text="⏺️", callback_data="none")
    button_pages5 = InlineKeyboardButton(text="назад", callback_data="none")
    if len(list_of_things) > 8:
        button_pages6 = InlineKeyboardButton(text="➡️", callback_data=thing_page_callback.new(thing_page_number=page,
                                                                                              thing_rotation="forward"))
    else:
        button_pages6 = InlineKeyboardButton(text="⏺️", callback_data="none")
    list_things_kb.row(button_pages4, button_pages5, button_pages6)
    return list_things_kb
