from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
                text='Узнать баланс',
                callback_data='balance_stats_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='График трат',
                callback_data='graphs_stats_button'
            )
        ]
    ]
)

back_stats_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Вернуться назад',
                callback_data='statistics_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Вернуться в меню',
                callback_data='menu_button'
            )
        ]
    ]
)

graphs_stats_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Расходы по категориям за выбранный период',
                callback_data='graph1_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Доходы за выбранный период',
                callback_data='graph2_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Назад',
                callback_data='statistics_button'
            )
        ]
    ]
)
