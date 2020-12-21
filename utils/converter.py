import datetime
from calendar import monthrange


def get_days_by_month() -> int:
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    return monthrange(year, month)[1]


def convert_to_budget(value: float, period: str) -> float:
    PERIODS = {
        'на день': 1,
        'на неделю': 7,
        'на месяц': get_days_by_month()
    }
    return round(value / PERIODS[period], 2)

