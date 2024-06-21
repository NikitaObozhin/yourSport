from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.morfotype.tests import morfotype_test
from app.morfotype.states import Morfotype
import app.morfotype.keyboards as kb


morfotypeRouter = Router()

# Выбор меню для определения морфотипа
@morfotypeRouter.callback_query(F.data == 'morfotype')
async def morfotype(callback: CallbackQuery):
    await callback.answer()
    await callback.message.reply(
        text="""Тест для определения морфтипа состоит из трех вопросов.
Вам необходимо знать свой рост, массу тела, а так же окружность грудной клетки в покое.

Начать выполнение?""", 
        reply_markup=kb.start_morfotype
        )

@morfotypeRouter.callback_query(F.data == 'chest_help')
async def chest_help(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
    text = """<b>Измерение окружности грудной клетки:</b>

1. Измерение осуществляется сантиметровой лентой в положении стоя, в состоянии покоя.
2. Необходимо освободить грудную клетку от одежды.
3. Сантиметровая лента накладывается сзади - по нижним углам лопаток (под лопатками), спереди - на уровне 4-го ребра:
- у мужчин - ниже сосков;
- у женщин - над основанием груди либо под грудными железами.
4. Лента накладывается плотно, но без натяжения.""",
        reply_markup=kb.back_or_start_morfotype,
        )

@morfotypeRouter.callback_query(F.data == 'back_morfotype')
async def back_morfotype(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
text="""Тест для определения морфтипа состоит из трех вопросов.
Вам необходимо знать свой рост, массу тела, а так же окружность грудной клетки в покое.

Начать выполнение?""", reply_markup=kb.start_morfotype
    )

@morfotypeRouter.callback_query(F.data == 'start_morfotype')
async def morfotype(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Morfotype.height)
    await callback.answer()
    await callback.message.answer('Вы начали проходить тест для определения морфотипа')
    await callback.message.answer('Введите длину тела (см)')


@morfotypeRouter.message(Morfotype.height)
async def morfotype_height(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    await state.set_state(Morfotype.weight)
    await message.answer('Введите массу тела (кг)')

@morfotypeRouter.message(Morfotype.weight)
async def morfotype_weight(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await state.set_state(Morfotype.chest)
    await message.answer('Введите охват груди в покое (см)')


@morfotypeRouter.message(Morfotype.chest)
async def morfotype_weight(message: Message, state: FSMContext):
    await state.update_data(chest=message.text)
    await message.answer(morfotype_test(await state.get_data()), reply_markup=kb.again_morfotype)
    await state.clear()