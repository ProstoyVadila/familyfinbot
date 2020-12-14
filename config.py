import os

from dotenv import load_dotenv


load_dotenv()

API_TOKEN = str(os.getenv('TELEGRAM_API_TOKEN'))
ADMIN_ID = str(os.getenv('ADMIN_ID'))
IP = os.getenv('IP')
PG_DATABASE = str(os.getenv('PG_DATABASE'))
PG_USER = str(os.getenv('PG_USER'))
PG_PASSWORD = str(os.getenv('PG_PASSWORD'))
PG_PORT = str(os.getenv('PG_PORT'))

POSTGRES_URI = f'postgresql://{PG_USER}:{PG_PASSWORD}@{IP}:{PG_PORT}/{PG_DATABASE}'

aiogram_redis = {
    'host': IP
}
redis = {
    'address': (IP, 6379),
    'encoding': 'utf8'
}