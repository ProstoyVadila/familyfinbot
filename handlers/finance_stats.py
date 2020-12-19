from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp, bot
from messages import finance, error
from keyboards.finance_keyboard import menu_keyboard
from keyboards.inline import finance_markups
from states.finance_states import IncomeState


GRAPHS_CALLBACK_DATA = ('graph1_button', 'graph2_button')


@dp.message_handler(commands=['stats'])
@dp.callback_query_handler(lambda callback: callback.data == 'statistics_button')
async def get_stats(types_object: Union[types.Message, types.CallbackQuery]):
    if isinstance(types_object, types.CallbackQuery):
        await types_object.answer(cache_time=60)
    await bot.send_message(
        types_object.from_user.id,
        finance.STATS_MESSAGE_START,
        reply_markup=finance_markups.stats_markup
    )


@dp.message_handler(commands=['balance'])
@dp.callback_query_handler(lambda callback: callback.data == 'balance_stats_button')
async def get_balance(types_object: Union[types.Message, types.CallbackQuery]):
    if isinstance(types_object, types.CallbackQuery):
        await types_object.answer(cache_time=60)

    await bot.send_message(
        types_object.from_user.id,
        finance.BALANCE_STATS_MESSAGE,
        reply_markup=finance_markups.back_stats_markup
    )


@dp.message_handler(commands=['graphs'])
@dp.callback_query_handler(lambda callback: callback.data == 'graphs_stats_button')
async def get_graph(types_object: Union[types.Message, types.CallbackQuery]):
    if isinstance(types_object, types.CallbackQuery):
        await types_object.answer(cache_time=60)

    await bot.send_message(
        types_object.from_user.id,
        finance.GRAPH_STATS_MESSAGE,
        reply_markup=finance_markups.graphs_stats_markup
    )


@dp.callback_query_handler(lambda callback: callback.data in GRAPHS_CALLBACK_DATA)
async def get_expanse_by_categories_graph(callback: types.CallbackQuery):
    await callback.answer(cache_time=60)
    await bot.send_message(
        callback.from_user.id,
        finance.YOUR_GRAPH_MESSAGE + f'\n your graph is {callback.data}',
        reply_markup=finance_markups.back_stats_markup
    )
