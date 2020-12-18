from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp, bot
from messages import base, error
from keyboards.finance_keyboard import expanse_category_keyboard, menu_keyboard
from states.finance_states import ExpanseState


@dp.message_handler(commands=['expanse'])
@dp.callback_query_handler(lambda callback: callback.data == 'expanse_button')
async def get_income(answer_object: Union[types.Message, types.CallbackQuery]):
    if isinstance(answer_object, types.CallbackQuery):
        await answer_object.answer(cache_time=60)
    await bot.send_message(
        answer_object.from_user.id,
        base.EXPANSE_MESSAGE_START
    )
    await ExpanseState.value.set()


@dp.message_handler(state=ExpanseState.value)
async def get_expanse_value(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['value'] = message.text
        await message.answer(
            base.EXPANSE_MESSAGE_END,
            reply_markup=expanse_category_keyboard
        )
        await ExpanseState.next()
    else:
        await message.answer(error.PARSE_INT_ERROR_MESSAGE)


@dp.message_handler(state=ExpanseState.category)
async def get_expanse_category(message: types.Message, state: FSMContext):
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
