from io import BytesIO
from datetime import date
from typing import Optional

from aiogram.types import InputFile

from models.db.transaction import Finance


DEFAULT_FIELD_NAMES = ['created_at', 'value', 'category', 'is_expense']
DEFAULT_DATE = date(2020, 1, 1)


async def upload_data_to_csv(user_id: int, from_date: date = DEFAULT_DATE, field_names=None) -> Optional[InputFile]:
    if field_names is None:
        field_names = DEFAULT_FIELD_NAMES

    columns = ','.join(field_names) + '\r\n'
    temp_list = []

    if data := await Finance.get_transactions(user_id=user_id, from_date=from_date):
        for item in data:
            temp_list.append(','.join([
                str(item.created_at),
                str(item.value),
                item.parent.category_name,
                str(item.is_expense)
            ]))
        output = columns + '\r\n'.join(temp_list)

        return InputFile(BytesIO(output.encode('utf8')), filename='your_data.csv')
