from typing import Union

from aiogram import types

from app import bot, dp
from controllers.finance.download_data import upload_data_to_csv, upload_data_to_xlsx
from utils.messages import finance
from utils.tools import answer_if_callback
from utils.keyboards.inline import finance_markups


async def send_file_if_data(user_id: int, file: types.InputFile):
    if not file:
        await bot.send_message(user_id, finance.DOWNLOADER_EMPTY_DATA_MESSAGE)
    else:
        await bot.send_document(user_id, file)


@dp.message_handler(commands=['download'])
@dp.callback_query_handler(lambda callback: callback.data == 'download_button')
async def download_data(msg_or_callback: Union[types.Message, types.CallbackQuery]):
    await answer_if_callback(msg_or_callback)
    await bot.send_message(
        msg_or_callback.from_user.id,
        finance.DOWNLOADER_START_MESSAGE,
        reply_markup=finance_markups.download_markup
    )


@dp.callback_query_handler(lambda callback: callback.data == 'csv_button')
async def download_csv(callback: types.CallbackQuery):
    await answer_if_callback(callback)
    await bot.send_message(callback.from_user.id, finance.DOWNLOADER_LOADING_MESSAGE)
    file = await upload_data_to_csv(callback.from_user.id)
    await send_file_if_data(callback.from_user.id, file)


@dp.callback_query_handler(lambda callback: callback.data == 'xlsx_button')
async def download_xlsx(callback: types.CallbackQuery):
    pass


@dp.message_handler(commands=['test'])
async def test_xlsx(msg: types.Message):
    file = await upload_data_to_xlsx(user_id=msg.from_user.id)
    await send_file_if_data(msg.from_user.id, file)
