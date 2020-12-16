from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

budget_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='На день',
                callback_data='budget_day_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='На неделю',
                callback_data='budget_week_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='На месяц',
                callback_data='budget_month_button'
            )
        ]
    ]
)
