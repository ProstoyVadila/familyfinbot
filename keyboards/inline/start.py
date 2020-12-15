from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_markup = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Начнем',
                callback_data='menu_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Подробнее',
                callback_data='about_button'
            )
        ]
    ]
)

