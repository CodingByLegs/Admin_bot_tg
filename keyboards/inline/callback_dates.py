from aiogram.utils.callback_data import CallbackData

category_callback = CallbackData("category", "category_name", "page")
page_callback = CallbackData("page", "page_number", "rotation")

thing_callback = CallbackData("thing", "thing_name", "thing_page")
thing_page_callback = CallbackData("thing_page", "thing_page_number", "thing_rotation")
