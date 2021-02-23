from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp, bot
from messages import finance, error
from model.models.transaction import Finance
from keyboards.finance_keyboard import expanse_category_keyboard, menu_keyboard
from states.finance_states import ExpenseState
from utils.extractors import parse_value
from utils.tools import answer_if_callback


@dp.message_handler(commands=['expense'])
@dp.callback_query_handler(lambda callback: callback.data == 'expense_button')
async def get_expense(msg_or_callback: Union[types.Message, types.CallbackQuery]):
    await answer_if_callback(msg_or_callback)
    await bot.send_message(
        msg_or_callback.from_user.id,
        finance.EXPENSE_MESSAGE_START
    )
    await ExpenseState.value.set()


@dp.message_handler(state=ExpenseState.value)
async def get_expense_value(message: types.Message, state: FSMContext):
    value = parse_value(message.text)
    if value:
        async with state.proxy() as data:
            data['value'] = value
        await message.answer(
            finance.EXPENSE_MESSAGE_END,
            reply_markup=expanse_category_keyboard
        )
        await ExpenseState.next()
    else:
        await message.answer(error.PARSE_VALUE_ERROR_MESSAGE)


@dp.message_handler(state=ExpenseState.category)
async def get_expense_category(message: types.Message, state: FSMContext):
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
        is_expense=True,
        category=data['category']
    )
    await state.finish()
