from datetime import date
from typing import Any, NamedTuple, List

from models.db.transaction import Finance
from models.db.user import User
from utils.converter import format_datetime_to_time
from utils.messages import finance


class BalanceData(NamedTuple):
    user_id: int
    budget: float
    from_date: date
    balance: float
    transactions_data: List[Any]


async def get_balance_by_id_by_date(user_id: int, from_date: date) -> BalanceData:
    expenses = 0
    transactions_data = []

    budget = await User.get_budget(user_id=user_id) if not None else 0
    transactions = await Finance.get_transactions(
        user_id=user_id,
        from_date=from_date,
        is_expense=True
    )

    if transactions:
        expenses = sum([item.value for item in transactions])
        transactions_data = transactions

    balance = budget - expenses
    return BalanceData(
        user_id=user_id,
        budget=budget,
        from_date=from_date,
        balance=balance,
        transactions_data=transactions_data
    )


def get_transaction_message(data: BalanceData) -> str:
    if not data.transactions_data:
        return finance.BALANCE_EMPTY_DATA_MESSAGE
    if data.budget == data.balance:
        return finance.BUDGET_EMPTY_DATA_MESSAGE

    data_format = '{created_at:10} --   {value:.2f} руб. -- {category:10}'
    data_message = '\n'.join([
        data_format.format(
            category=item.parent.category_name,
            value=item.value,
            created_at=format_datetime_to_time(item.created_at)
        )
        for item in data.transactions_data
    ])
    return finance.BALANCE_TRANS_DATA_MESSAGE + data_message
