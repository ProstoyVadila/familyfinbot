from aiogram.dispatcher.filters.state import State, StatesGroup


class BudgetState(StatesGroup):
    period = State()
    value = State()


class ExpanseState(StatesGroup):
    value = State()
    category = State()


class IncomeState(StatesGroup):
    value = State()
    category = State()


# rewrite to other state file
class FeedbackState(StatesGroup):
    message = State()
