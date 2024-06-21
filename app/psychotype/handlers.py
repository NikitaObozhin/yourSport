from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import app.psychotype.questions as qu
import app.psychotype.keyboards as kb
from app.psychotype.states import Psychotype
from app.psychotype.tests import set_result_psychotype

psychotypeRouter = Router()

@psychotypeRouter.callback_query(F.data == 'psychotype')
async def psychotype(callback: CallbackQuery):
    await callback.answer()
    await callback.message.reply(
        text="""Тест на определение темперамента состоит из 12 вопросов.
Примерное время прохождения теста &lt; 1 минуты.

Каждый вопрос необходимо внимательно прочитать и долго не раздумывать об ответе.
Начать выполнение?""",
        reply_markup=kb.start_psychotype
)

@psychotypeRouter.callback_query(F.data == 'start_psychotype')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Psychotype.question_1)
    await callback.answer()
    await callback.message.reply(
        text=qu.questions[0],
        reply_markup=kb.answers_1
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A1' or call.data == 'B1' or call.data == 'C1' or call.data == 'D1')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_1=callback.data[0])
    await state.set_state(Psychotype.question_2)
    await callback.answer()
    await callback.message.edit_text(
        text=qu.questions[1],
        reply_markup=kb.answers_2
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A2' or call.data == 'B2' or call.data == 'C2' or call.data == 'D2')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_2=callback.data[0])
    await state.set_state(Psychotype.question_3)
    await callback.answer()
    await callback.message.edit_text(
        text=qu.questions[2],
        reply_markup=kb.answers_3
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A3' or call.data == 'B3' or call.data == 'C3' or call.data == 'D3')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_3=callback.data[0])
    await state.set_state(Psychotype.question_4)
    await callback.answer()
    await callback.message.edit_text(
        text=qu.questions[3],
        reply_markup=kb.answers_4
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A4' or call.data == 'B4' or call.data == 'C4' or call.data == 'D4')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_4=callback.data[0])
    await state.set_state(Psychotype.question_5)
    await callback.answer()
    await callback.message.edit_text(
        text=qu.questions[4],
        reply_markup=kb.answers_5
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A5' or call.data == 'B5' or call.data == 'C5' or call.data == 'D5')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_5=callback.data[0])
    await state.set_state(Psychotype.question_6)
    await callback.answer()
    await callback.message.edit_text(
        text=qu.questions[5],
        reply_markup=kb.answers_6
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A6' or call.data == 'B6' or call.data == 'C6' or call.data == 'D6')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_6=callback.data[0])
    await state.set_state(Psychotype.question_7)
    await callback.answer()
    await callback.message.edit_text(
        text=qu.questions[6],
        reply_markup=kb.answers_7
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A7' or call.data == 'B7' or call.data == 'C7' or call.data == 'D7')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_7=callback.data[0])
    await state.set_state(Psychotype.question_8)
    await callback.answer()
    await callback.message.edit_text(
        text=qu.questions[7],
        reply_markup=kb.answers_8
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A8' or call.data == 'B8' or call.data == 'C8' or call.data == 'D8')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_8=callback.data[0])
    await state.set_state(Psychotype.question_9)
    await callback.answer()
    await callback.message.edit_text(
        text=qu.questions[8],
        reply_markup=kb.answers_9
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A9' or call.data == 'B9' or call.data == 'C9' or call.data == 'D9')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_9=callback.data[0])
    await state.set_state(Psychotype.question_10)
    await callback.answer()
    await callback.message.edit_text(
        text=qu.questions[9],
        reply_markup=kb.answers_10
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A10' or call.data == 'B10' or call.data == 'C10' or call.data == 'D10')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_10=callback.data[0])
    await state.set_state(Psychotype.question_11)
    await callback.answer()
    await callback.message.edit_text(
        text=qu.questions[10],
        reply_markup=kb.answers_11
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A11' or call.data == 'B11' or call.data == 'C11' or call.data == 'D11')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_11=callback.data[0])
    await state.set_state(Psychotype.question_12)
    await callback.answer()
    await callback.message.edit_text(
        text=qu.questions[11],
        reply_markup=kb.answers_12
    )

@psychotypeRouter.callback_query(lambda call: call.data == 'A12' or call.data == 'B12' or call.data == 'C12' or call.data == 'D12')
async def start_psychotype(callback: CallbackQuery, state: FSMContext):
    await state.update_data(question_12=callback.data[0])
    await callback.answer()
    await callback.message.edit_text(
        text = set_result_psychotype(await state.get_data()),
        reply_markup=kb.start_psychotype_again
        )
    await state.clear()
 