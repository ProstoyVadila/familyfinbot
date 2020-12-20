from sqlalchemy import sql

from model.db_gino import db, TimeBaseModel


class User(TimeBaseModel):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer(), primary_key=True, index=True)
    user_name = db.Column(db.Unicode())
    user_budget = db.Column(db.Integer())

    query: sql.Select

    @classmethod
    async def get_or_create(cls, user_id: int, name: str = None) -> "User":
        user = await cls.get(user_id)
        if not user:
            return await cls.create(user_id=user_id, user_name=name)
        return user
