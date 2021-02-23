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

expanse_category_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Транспорт'),
            KeyboardButton(text='Продукты'),
            KeyboardButton(text='Развлечения'),
        ],
        [
            KeyboardButton(text='Связь'),
            KeyboardButton(text='Налоги'),
            KeyboardButton(text='Образование'),
        ],
        [
            KeyboardButton(text='Быт'),
            KeyboardButton(text='Подарки'),
            KeyboardButton(text='Помощь')
        ],
        [
            KeyboardButton(text='Без категории')
        ],
    ],
    resize_keyboard=True
)

income_category_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Зарплата'),
            KeyboardButton(text='Фриланс'),
            KeyboardButton(text='Долг'),
        ],
        [
            KeyboardButton(text='Пособие'),
            KeyboardButton(text='Кешбек'),
            KeyboardButton(text='Кредит'),
        ],
        [
            KeyboardButton(text='Без категории')
        ],
    ],
    resize_keyboard=True
)
