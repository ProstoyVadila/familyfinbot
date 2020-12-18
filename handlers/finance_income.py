from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp, bot
from messages import base, error
from keyboards.finance_keyboard import income_category_keyboard, menu_keyboard
from states.finance_states import IncomeState


@dp.message_handler(commands=['income'])
@dp.callback_query_handler(lambda callback: callback.data == 'income_button')
async def get_income(answer_object: Union[types.Message, types.CallbackQuery]):
    if isinstance(answer_object, types.CallbackQuery):
        await answer_object.answer(cache_time=60)

    await bot.send_message(
        answer_object.from_user.id,
        base.INCOME_MESSAGE_START
    )
    await IncomeState.value.set()


@dp.message_handler(state=IncomeState.value)
async def get_income_value(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['value'] = message.text
        await message.answer(
            base.INCOME_MESSAGE_END,
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
        base.YOUR_TRANSACTION_MESSAGE.format(
            value=data['value'],
            category=data['category']
        ),
        reply_markup=menu_keyboard
    )
    await state.finish()
