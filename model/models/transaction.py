from datetime import date, datetime, time
from typing import List

from sqlalchemy import sql

from model.db_gino import db, TimeBaseModel

from .user import User
from .category import Category


def is_more_than_period(time: date) -> bool:
    pass


class Finance(TimeBaseModel):
    __tablename__ = 'finance'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(None, db.ForeignKey('users.user_id'), nullable=False)
    value = db.Column(db.Integer(), nullable=False)
    is_expense = db.Column(db.Boolean(), nullable=False)
    category_id = db.Column(None, db.ForeignKey('categories.category_id'))

    query: sql.Select

    @classmethod
    async def add_transaction(cls, user_id: int, value: int,
                              is_expense: bool, category: str):
        await User.get_or_create(user_id)
        category_from_db = await Category.get_or_create(category, is_expense)
        await cls.create(
            user_id=user_id,
            value=value,
            is_expense=is_expense,
            category_id=category_from_db.category_id
        )

    @classmethod
    async def get_transactions(cls, user_id: int, from_date: date, is_expense: bool) -> List['Finance']:
        transactions = await Finance.query.where(
            Finance.user_id == user_id
        ).where(
            Finance.is_expense == is_expense
        ).where(
            Finance.created_at >= datetime.combine(from_date, time(0, 0))
        ).gino.all()
        return transactions

    @classmethod
    async def get_balance(cls, user_id) -> [float, float]:
        budget = await User.get_budget(user_id)
        transactions = await cls.get_transactions(user_id, date.today(), True)
        expenses = sum([item.value for item in transactions])
        balance = budget - expenses
        return balance, budget

    @classmethod
    async def save_csv(cls, user_id: int):
        pass
