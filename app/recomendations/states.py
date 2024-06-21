from aiogram.fsm.state import State, StatesGroup

class Recomendations(StatesGroup):
    morfotype = State()
    psychotype = State()