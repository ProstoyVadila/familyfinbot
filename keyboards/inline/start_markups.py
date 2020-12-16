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

menu_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Установить бюджет',
                callback_data='budget_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Внести расход',
                callback_data='expanse_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Внести доход',
                callback_data='income_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Получить статистику',
                callback_data='statistics_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Выгрузить свои данные',
                callback_data='download_data_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Вернуться назад',
                callback_data='return_to_start_button'
            )
        ]
    ]
)
