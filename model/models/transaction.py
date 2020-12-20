from sqlalchemy import sql

from model.db_gino import db, TimeBaseModel


class Finance(TimeBaseModel):
    __tablename__ = 'finance'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(None, db.ForeignKey('users.user_id'), nullable=False)
    value = db.Column(db.Integer(), nullable=False)
    is_expanse = db.Column(db.Boolean(), nullable=False)
    category_id = db.Column(None, db.ForeignKey('categories.category_id'))

    query: sql.Select
