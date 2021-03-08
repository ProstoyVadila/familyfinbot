import os

from dotenv import load_dotenv


load_dotenv()

API_TOKEN = str(os.getenv('TELEGRAM_API_TOKEN'))
ADMIN_ID = str(os.getenv('ADMIN_ID'))
HOST = os.getenv('HOST')
PG_DATABASE = str(os.getenv('PG_DATABASE'))
PG_USER = str(os.getenv('PG_USER'))
PG_PASSWORD = str(os.getenv('PG_PASSWORD'))
PG_PORT = str(os.getenv('PG_PORT'))
IP = str(os.getenv('IP'))

POSTGRES_URI_TEST = f'postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{IP}/{PG_DATABASE}'
POSTGRES_URI = f'postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{HOST}/{PG_DATABASE}'

aiogram_redis = {
    'host': HOST
}
redis = {
    'address': (HOST, 6379),
    'encoding': 'utf8'
}

DONATE_URL_90 = 'https://capu.st/bill5c849142-1478'
DONATE_URL = 'https://capu.st/bill70918ae8-cd9e'
