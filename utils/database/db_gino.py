import datetime
import logging
from typing import List

import sqlalchemy as sa
from aiogram import Dispatcher
from gino import Gino

from config import POSTGRES_URI


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
        db.DataTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=db.func.now()
    )


async def on_startup(dp: Dispatcher):
    logging.info('Connecting to PostgreSQL')
    await db.set_bind(POSTGRES_URI)


async def on_shutdown(dp: Dispatcher):
    logging.info('Connection to PostgreSQL was closed')
    await db.close()