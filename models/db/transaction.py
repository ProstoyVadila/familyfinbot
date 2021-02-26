from datetime import date, datetime, time
from typing import List

from sqlalchemy import sql

from models.db_gino import db, TimeBaseModel

from .user import User
from .category import Category


class Finance(TimeBaseModel):
    __tablename__ = 'finance'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(None, db.ForeignKey('users.user_id'), nullable=False)
    value = db.Column(db.Float(), nullable=False)
    is_expense = db.Column(db.Boolean(), nullable=False)
    category_id = db.Column(None, db.ForeignKey('categories.category_id'))

    query: sql.Select

    @classmethod
    async def add_transaction(cls, user_id: int, value: float,
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
    async def get_transactions(cls, user_id: int, from_date: date, is_expense: bool = None) -> List['Finance']:
        loader = cls.load(parent=Category.on(cls.category_id == Category.category_id))

        if is_expense is None:
            return await loader.query.where(
                cls.user_id == user_id
            ).where(
                cls.created_at >= datetime.combine(from_date, time(0, 0))
            ).gino.all()

        return await loader.query.where(
            cls.user_id == user_id
        ).where(
            cls.is_expense == is_expense
        ).where(
            cls.created_at >= datetime.combine(from_date, time(0, 0))
        ).gino.all()
