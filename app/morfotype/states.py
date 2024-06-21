from aiogram.fsm.state import State, StatesGroup

class Morfotype(StatesGroup):
    height = State()
    weight = State()
    chest = State()