from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp, bot
from utils.messages import finance, error
from models.db.user import User
from utils.keyboards.finance_keyboard import budget_keyboard
from utils.keyboards.inline.start_markups import back_to_menu_markup
from models.states.finance_states import BudgetState
from utils.extractors import parse_value
from utils.tools import answer_if_callback


@dp.message_handler(commands=['budget'])
@dp.callback_query_handler(lambda callback: callback.data == 'budget_button')
async def get_budget(msg_or_callback: Union[types.Message, types.CallbackQuery]):
    await answer_if_callback(msg_or_callback)
    await bot.send_message(
        msg_or_callback.from_user.id,
        finance.BUDGET_MESSAGE_START,
        reply_markup=budget_keyboard
    )
    await BudgetState.period.set()


@dp.message_handler(state=BudgetState.period)
async def get_budget_period(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['period'] = message.text

    await message.answer(
        finance.BUDGET_MESSAGE_END,
        reply_markup=types.ReplyKeyboardRemove()
    )
    await BudgetState.next()


@dp.message_handler(state=BudgetState.value)
async def get_budget_value(message: types.Message, state: FSMContext):
    value = parse_value(message.text)
    if value:
        async with state.proxy() as data:
            data['value'] = value

        await User.update_budget(
            user_id=message.from_user.id,
            value=data['value'],
            period=data['period']
        )
        await message.answer(
            finance.YOUR_BUDGET_MESSAGE.format(
                value=data['value'],
                period=data['period']
            ),
            reply_markup=back_to_menu_markup
        )
        await state.finish()
    else:
        await message.answer(error.PARSE_VALUE_ERROR_MESSAGE)
