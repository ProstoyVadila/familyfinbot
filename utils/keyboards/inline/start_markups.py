from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from emoji import emojize

start_markup = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Начнем  ' + emojize(':rocket:'),
                callback_data='menu_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Подробнее  ' + emojize(':notebook:'),
                callback_data='about_button'
            )
        ]
    ]
)

menu_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Узнать баланс  '
                    + emojize(':credit_card:'),
                callback_data='balance_stats_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Внести расход  '
                     + emojize(':chart_decreasing:'),
                callback_data='expense_button'
            ),
            InlineKeyboardButton(
                text='Внести доход  '
                     + emojize(':chart_increasing:'),
                callback_data='income_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Установить бюджет  '
                     + emojize(':money_bag:'),
                callback_data='budget_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Получить статистику  '
                     + emojize(':bar_chart:'),
                callback_data='statistics_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Выгрузить свои данные  '
                     + emojize(':floppy_disk:'),
                callback_data='download_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Пожертвовать на развитие  '
                     + emojize(':rocket:'),
                callback_data='donate_button'
            )
        ]
    ]
)

back_to_menu_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='В меню  '
                     + emojize(':BACK_arrow:'),
                callback_data='menu_button'
            )
        ]
    ]
)
