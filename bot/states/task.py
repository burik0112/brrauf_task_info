from aiogram.fsm.state import State, StatesGroup


class TaskState(StatesGroup):
    collecting_tasks = State()
    confirming_tasks = State()
