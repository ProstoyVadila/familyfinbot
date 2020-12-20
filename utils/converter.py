
def convert_to_budget(value: float, period: str) -> float:
    PERIODS = {
        'на день': 1,
        'на неделю': 7,
        'на месяц': 30.5
    }
    return round(value / PERIODS[period], 2)

