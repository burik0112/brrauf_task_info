from aiogram.fsm.state import State, StatesGroup


class TaskState(StatesGroup):
    collecting_tasks = State()
    waiting_for_responsible = State()
    waiting_for_responsible_search = State()
    confirming_tasks = State()
