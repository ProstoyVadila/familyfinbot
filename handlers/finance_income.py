from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp, bot
from utils.messages import finance, error
from models.db.transaction import Finance
from utils.keyboards.finance_keyboard import income_category_keyboard, menu_keyboard
from models.states.finance_states import IncomeState
from utils.extractors import parse_value
from utils.tools import answer_if_callback


@dp.message_handler(commands=['income'])
@dp.callback_query_handler(lambda callback: callback.data == 'income_button')
async def get_income(msg_or_callback: Union[types.Message, types.CallbackQuery]):
    await answer_if_callback(msg_or_callback)

    await bot.send_message(
        msg_or_callback.from_user.id,
        finance.INCOME_MESSAGE_START
    )
    await IncomeState.value.set()


@dp.message_handler(state=IncomeState.value)
async def get_income_value(message: types.Message, state: FSMContext):
    value = parse_value(message.text)
    if value:
        async with state.proxy() as data:
            data['value'] = value
        await message.answer(
            finance.INCOME_MESSAGE_END,
            reply_markup=income_category_keyboard
        )
        await IncomeState.next()
    else:
        await message.answer(error.PARSE_VALUE_ERROR_MESSAGE)


@dp.message_handler(state=IncomeState.category)
async def get_income_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer(
        finance.YOUR_TRANSACTION_MESSAGE.format(
            value=data['value'],
            category=data['category']
        ),
        reply_markup=menu_keyboard
    )
    await Finance.add_transaction(
        user_id=message.from_user.id,
        value=data['value'],
        is_expense=False,
        category=data['category']
    )
    await state.finish()
