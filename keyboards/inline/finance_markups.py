from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji as e

budget_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='на день',
                callback_data='day_budget_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='на неделю',
                callback_data='week_budget_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='на месяц',
                callback_data='month_budget_button'
            )
        ]
    ]
)

stats_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Узнать баланс  '
                     + e.emojize(':credit_card:'),
                callback_data='balance_stats_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='График трат  '
                     + e.emojize(':chart_increasing_with_yen:'),
                callback_data='graphs_stats_button'
            )
        ]
    ]
)

back_stats_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Вернуться назад  '
                     + e.emojize(':BACK_arrow:'),
                callback_data='statistics_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Вернуться в меню  '
                     + e.emojize(':page_with_curl:'),
                callback_data='menu_button'
            )
        ]
    ]
)

graphs_stats_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Мои расходы по категориям  '
                     + e.emojize(':bar_chart:'),
                callback_data='graph1_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Мои доходы по категориям  '
                     + e.emojize(':bar_chart:'),
                callback_data='graph2_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Назад  '
                     + e.emojize(':BACK_arrow:'),
                callback_data='statistics_button'
            )
        ]
    ]
)
