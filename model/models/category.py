from typing import Optional, List

from sqlalchemy import sql

from model.db_gino import db, TimeBaseModel


class Category(TimeBaseModel):
    __tablename__ = 'categories'

    category_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(), nullable=False)
    is_expense = db.Column(db.Boolean(), nullable=False)

    query: sql.Select

    @classmethod
    async def get_or_create(cls, name: str, is_expense: bool) -> ['Category']:
        category = await cls.query.where(cls.category_name == name).gino.first()
        if not category:
            return await cls.create(
                category_name=name,
                is_expense=is_expense
            )
        return category

    @classmethod
    async def get_category_by_id(cls, id_: int) -> Optional['Category']:
        return await cls.query.where(cls.category_id == id_).gino.first()

    @classmethod
    async def get_category_names_by_ids(cls, ids: List[int]) -> Optional[List[str]]:
        categories = [
            await cls.get_category_by_id(id_)
            for id_ in ids
            if cls.get_category_by_id(id_) is not None
        ]
        return [item.category_name for item in categories]
