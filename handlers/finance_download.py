from aiogram import types

from app import bot, dp
from controllers.finance.download_data import upload_data_to_csv
from utils.messages import finance


@dp.message_handler(commands=['test'])
async def download_csv(message: types.Message):
    await message.answer('Загружаю данные... Это может занять некоторое время')
    file = await upload_data_to_csv(message.from_user.id)
    if not file:
        await message.answer(message.from_user.id, finance.DOWNLOADER_EMPTY_DATA_MESSAGE)
    else:
        await bot.send_document(message.from_user.id, file)
