from sqlalchemy import sql

from model.db_gino import db, TimeBaseModel


class Category(TimeBaseModel):
    __tablename__ = 'categories'

    category_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(), nullable=False)
    is_expense = db.Column(db.String(), nullable=False)
    category_aliases = db.Column(db.Text())

    query: sql.Select
