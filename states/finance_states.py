from aiogram.dispatcher.filters.state import State, StatesGroup


class BudgetState(StatesGroup):
    period = State()
    value = State()
