from io import BytesIO
from datetime import date
from typing import List, Optional, Tuple

from aiogram.types import InputFile
import pandas as pd

from models.db.transaction import Finance
from utils.exceptions import FileFormatError

DEFAULT_FIELD_NAMES = ('created_at', 'value', 'category', 'is_expense')
DEFAULT_DATE = date(2020, 1, 1)
FILE_FORMATS = ('csv', 'xlsx')


# async def upload_data(user_id: int, file_format: str, from_date: date = DEFAULT_DATE,
#                       field_names: Tuple = DEFAULT_FIELD_NAMES) -> Optional[InputFile]:
#     if file_format not in FILE_FORMATS:
#         raise FileFormatError(file_format)
#
#     if user_data := await Finance.get_transactions(user_id=user_id, from_date=from_date):
#         pass


async def upload_data_to_xlsx(user_id: int, from_date: date = DEFAULT_DATE, field_names=None) -> Optional[InputFile]:
    if field_names is None:
        field_names = DEFAULT_FIELD_NAMES

    if data := await Finance.get_transactions(user_id=user_id, from_date=from_date):
        df = pd.DataFrame({'Data': [10, 20, 30, 40, 50]})
        output = BytesIO()
        with pd.ExcelWriter(output) as writer:
            df.to_excel(writer)
            writer.save()
            output.seek(0)
            return InputFile(output, filename='your_data.xlsx')


async def upload_data_to_csv(user_id: int, from_date: date = DEFAULT_DATE, field_names=None) -> Optional[InputFile]:
    if field_names is None:
        field_names = DEFAULT_FIELD_NAMES

    if data := await Finance.get_transactions(user_id=user_id, from_date=from_date):
        output = construct_csv(data, field_names)
        return InputFile(BytesIO(output.encode('utf8')), filename='your_data.csv')


def construct_csv(data: List[Finance], field_names: str) -> str:
    columns = ','.join(field_names) + '\r\n'
    temp_list = []

    for item in data:
        temp_list.append(','.join([
            str(item.created_at),
            str(item.value),
            item.parent.category_name,
            str(item.is_expense)
        ]))
    return columns + '\r\n'.join(temp_list)
