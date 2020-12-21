from sqlalchemy import sql

from model.db_gino import db, TimeBaseModel


class Category(TimeBaseModel):
    __tablename__ = 'categories'

    category_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(), nullable=False)
    is_expense = db.Column(db.Boolean(), nullable=False)

    query: sql.Select

    @classmethod
    async def get_or_get_category(cls, name: str, is_expense: bool):
        category = await cls.query.where(cls.category_name == name).gino.first()
        if not category:
            return await cls.create(
                category_name=name,
                is_expense=is_expense
            )
        return category
