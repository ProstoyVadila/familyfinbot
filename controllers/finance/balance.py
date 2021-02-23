from datetime import date
from typing import Any, NamedTuple, List

from utils.messages import finance
from models.db.category import Category
from models.db.transaction import Finance
from models.db.user import User

from utils.converter import format_datetime_to_time


class BalanceData(NamedTuple):
    user_id: int
    budget: float
    from_date: date
    balance: float
    transactions_data: List[Any]


async def get_balance_by_id_by_date(user_id: int, from_date: date) -> BalanceData:
    budget = await User.get_budget(user_id=user_id)
    transactions = await Finance.get_transactions(
        user_id=user_id,
        from_date=from_date,
        is_expense=True
    )
    if not budget:
        budget = 0
    if not transactions:
        balance = budget,
        transactions_data = []
    else:
        balance = budget - sum([item.value for item in transactions])
        categories_ids = [item.category_id for item in transactions]
        categories_names = await Category.get_category_names_by_ids(categories_ids)
        transactions_data = list(zip(transactions, categories_names))

    return BalanceData(
        user_id=user_id,
        budget=budget,
        from_date=from_date,
        balance=balance,
        transactions_data=transactions_data
    )


def get_transaction_message(data: BalanceData.transactions_data) -> str:
    if not data:
        return finance.BALANCE_EMPTY_DATA_MESSAGE

    data_format = '{created_at:10} --   {value:.2f} руб. -- {category:10}'
    data_message = '\n'.join([
        data_format.format(
            category=item[1],
            value=item[0].value,
            created_at=format_datetime_to_time(item[0].created_at)
        )
        for item in data
    ])
    return finance.BALANCE_TRANS_DATA_MESSAGE + data_message
