from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji as e

start_markup = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Начнем  ' + e.emojize(':rocket:'),
                callback_data='menu_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Подробнее  ' + e.emojize(':notebook:'),
                callback_data='about_button'
            )
        ]
    ]
)

menu_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Установить бюджет  ' \
                + e.emojize(':money_bag:'),
                callback_data='budget_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Внести расход  ' \
                + e.emojize(':chart_decreasing:'),
                callback_data='expense_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Внести доход  ' \
                + e.emojize(':chart_increasing:'),
                callback_data='income_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Получить статистику  ' \
                     + e.emojize(':bar_chart:'),
                callback_data='statistics_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Выгрузить свои данные  ' \
                     + e.emojize(':floppy_disk:'),
                callback_data='download_data_button'
            )
        ],
    ]
)

back_to_menu_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Вернуться в меню  ' \
                + e.emojize(':BACK_arrow:'),
                callback_data='menu_button'
            )
        ]
    ]
)
