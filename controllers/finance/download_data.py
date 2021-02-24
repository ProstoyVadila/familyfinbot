import csv
import os
from datetime import date

from aiogram.types import InputFile

from models.db.transaction import Finance


async def download_file_csv(user_id: int) -> InputFile:
    from_date = date(2020, 1, 1)
    data = await Finance.get_transactions(user_id=user_id, from_date=from_date, is_expense=True)
    fieldnames = ['created_at', 'value', 'category', 'is_expense']
    with open(f'utils/temporary_files/{user_id}.csv', 'w') as csvfile:
        writer_ = csv.writer(csvfile)
        writer_.writerow(fieldnames)
        for item in data:
            writer_.writerow([item.created_at, item.value, item.parent.category_name, item.is_expense])

    return InputFile(f'utils/temporary_files/{user_id}.csv', filename='your_data.csv')


async def delete_file(filename: str):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../utils/temporary_files/' + filename)
    os.remove(path)
