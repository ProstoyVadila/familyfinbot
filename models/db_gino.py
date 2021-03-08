import logging
from typing import List

import sqlalchemy as sa
from aiogram import Dispatcher
from gino import Gino

import config


db = Gino()


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in table.columns
        }
        values_str = ' '.join(
            f'{name}={value!r}' for name, value in values.items()
        )
        return f'<{model} {values_str}>'


class TimeBaseModel(BaseModel):
    __abstract__ = True

    created_at = db.Column(db.DateTime(True), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(True),
        default=db.func.now(),
        onupdate=db.func.now(),
        server_default=db.func.now()
    )


async def on_startup():
    logging.info('Connecting to PostgreSQL')
    await db.set_bind(config.POSTGRES_URI_TEST)
    # await db.gino.drop_all()
    await db.gino.create_all()


async def on_shutdown():
    await db.pop_bind().close()
    logging.info('Connection to PostgreSQL was closed')
