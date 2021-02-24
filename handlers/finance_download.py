from aiogram import types

from app import bot, dp
from controllers.finance.download_data import download_file_csv, delete_file


@dp.message_handler(commands=['test'])
async def download_csv(message: types.Message):
    file = await download_file_csv(user_id=message.from_user.id)
    await message.answer('Загружаю данные... Это может занять некоторое время')
    await bot.send_document(message.from_user.id, file)
    await delete_file(f'{message.from_user.id}.csv')
