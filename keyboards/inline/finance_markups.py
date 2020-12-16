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
