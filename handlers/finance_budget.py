from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp, bot
from messages import base, error
from keyboards.finance_keyboard import budget_keyboard
from keyboards.inline.start_markups import back_to_menu_markup
from states.finance_states import BudgetState
from utils.extractors import parse_value


PERIODS = {
    'на день': 'day',
    'на неделю': 'week',
    'на месяц': 'month'
}


@dp.message_handler(commands=['budget'])
@dp.callback_query_handler(lambda callback: callback.data == 'budget_button')
async def get_budget(answer_object: Union[types.Message, types.CallbackQuery]):
    if isinstance(answer_object, types.CallbackQuery):
        await answer_object.answer(cache_time=60)
    await bot.send_message(
        answer_object.from_user.id,
        base.BUDGET_MESSAGE_START,
        reply_markup=budget_keyboard
    )
    await BudgetState.period.set()


@dp.message_handler(state=BudgetState.period)
async def get_budget_period(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['period'] = message.text

    await message.answer(
        base.BUDGET_MESSAGE_END,
        reply_markup=types.ReplyKeyboardRemove()
    )
    await BudgetState.next()


@dp.message_handler(state=BudgetState.value)
async def get_budget_value(message: types.Message, state: FSMContext):
    value = parse_value(message.text)
    if value:
        async with state.proxy() as data:
            data['value'] = value
        await message.answer(
            base.YOUR_BUDGET_MESSAGE.format(
                value=data['value'],
                period=data['period']
            ),
            reply_markup=back_to_menu_markup
        )
        await state.finish()
    else:
        await message.answer(error.PARSE_VALUE_ERROR_MESSAGE)
