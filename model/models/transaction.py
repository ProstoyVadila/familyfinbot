from sqlalchemy import sql

from model.db_gino import db, TimeBaseModel

from .user import User
from .category import Category


class Finance(TimeBaseModel):
    __tablename__ = 'finance'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(None, db.ForeignKey('users.user_id'), nullable=False)
    value = db.Column(db.Integer(), nullable=False)
    is_expanse = db.Column(db.Boolean(), nullable=False)
    category_id = db.Column(None, db.ForeignKey('categories.category_id'))

    query: sql.Select

    @classmethod
    async def add_transaction(cls, user_id: int, value: int,
                              is_expanse: bool, category: str):
        user = await User.get_or_create(user_id)
        category_from_db = await Category.get_or_get_category(category, is_expanse)
        await cls.create(
            user_id=user_id,
            value=value,
            is_expanse=is_expanse,
            category_id=category_from_db.category_id
        )
