from utils.database.db_gino import db, TimeBaseModel


class User(TimeBaseModel):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    telegram_id = db.Column(db.Integer(), nullable=False)
    user_name = db.Column(db.Unicode())
    user_budget = db.Column(db.Integer())
