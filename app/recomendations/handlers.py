from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.recomendations.states import Recomendations
import app.recomendations.keyboards as kb
from app.recomendations.tests import recomendations_
import app.keyboards as kb_main

recomendationsRouter = Router()

@recomendationsRouter.message(F.text == 'Рекомендации')
async def rec_morfotype(message: Message, state: FSMContext):
    await state.set_state(Recomendations.morfotype)
    await message.answer(
            text='''Сейчас у вас есть возможность получить рекомендации на основе вашего психотипа и мофротипа.
Если вы их не знаете, выберите меню 'Показатели' и пройдите тесты.

Выберите свой морфотип:''',
            reply_markup=kb.morfotype
    )

@recomendationsRouter.callback_query(lambda call: call.data == 'asten' or call.data == 'normosten' or call.data  == 'hypersten') 
async def rec_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(morfotype=callback.data)
    await state.set_state(Recomendations.psychotype)
    await callback.answer()
    await callback.message.edit_text(
        text='Выберите свой психотип',
        reply_markup=kb.psychotype
    )

@recomendationsRouter.callback_query(lambda call: call.data == 'holer' or call.data == 'fleg' or call.data == 'sang' or call.data == 'melan')
async def rec_result(callback: CallbackQuery, state: FSMContext):
    await state.update_data(psychotype=callback.data)
    await callback.answer()
    await callback.message.edit_text(
        text=recomendations_(await state.get_data())
    )
    await state.clear()
