from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from emoji import emojize

from config import DONATE_URL, DONATE_URL_90


donate_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='90 рублей  ' + emojize(':rocket:'),
                url=DONATE_URL_90,
                callback_data='donate_done_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Другая сумма  ' + emojize(':rocket::rocket::rocket:'),
                url=DONATE_URL,
                callback_data='donate_done_button'
            )
        ],
        [
            InlineKeyboardButton(
                text='Назад  ' + emojize(':BACK_arrow:'),
                callback_data='menu_button'
            )
        ]
    ]
)