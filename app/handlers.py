from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command


import app.keyboards as kb

mainRouter = Router()

# начало работы с ботом
@mainRouter.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}! Я твой спортивный помощник.', reply_markup=kb.main)


# Выбор меню показатели
@mainRouter.message(F.text == 'Показатели')
async def parameters(message: Message):
    await message.reply('Выберите какой показатель необходимо рассчитать', reply_markup=kb.parameters)


@mainRouter.message(F.text == 'О боте')
async def about(message: Message):
    await message.reply('Данный бот создан, чтобы упростить выбор направления физической культуры студентам Тюменского государственного университета. Зная свой морфотип и психотип вы сможете получить рекомендацию по выбору направления, если вы их не знаете, то сможете рассчитать их прямо тут.')

# @mainRouter.callback_query(F.data == 'parameters')
# async def parameters(callback: CallbackQuery, message: Message):
#     await callback.answer()
#     await message.reply('Выберите какой показатель необходимо рассчитать', reply_markup=kb.parameters)