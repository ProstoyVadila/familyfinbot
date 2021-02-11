from sqlalchemy import sql

from model.db_gino import db, TimeBaseModel
from utils.converter import convert_to_budget


class User(TimeBaseModel):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer(), primary_key=True, index=True)
    user_name = db.Column(db.Unicode())
    user_budget = db.Column(db.Float())

    query: sql.Select

    @classmethod
    async def get_or_create(cls, user_id: int, name: str = None) -> "User":
        user = await cls.get(user_id)
        if not user:
            return await cls.create(user_id=user_id, user_name=name)
        return user

    @classmethod
    async def update_budget(cls, user_id: int, value: float, period: str):
        user = await cls.get_or_create(user_id)
        budget = convert_to_budget(value, period)
        await user.update(user_budget=budget).apply()

    @classmethod
    async def get_budget(cls, user_id) -> float:
        user = await cls.get_or_create(user_id)
        return user.user_budget

    # @classmethod
    # async def get_balance(cls, user_id) -> float:
    #     budget = cls.get_budget(user_id)
    #     transactions = Finance.get_transactions(user_id, "24", True)
    #     print(f'\n\n_______________{transactions}\n\n_______________\n\n{type(transactions)}')
    #     return budget
