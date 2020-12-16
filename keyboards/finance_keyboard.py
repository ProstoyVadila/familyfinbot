from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='меню')
        ]
    ],
    resize_keyboard=True
)

budget_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='на день')
        ],
        [
            KeyboardButton(text='на неделю')
        ],
        [
            KeyboardButton(text='на месяц')
        ]
    ],
    resize_keyboard=True
)