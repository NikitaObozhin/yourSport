from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


back_or_start_morfotype = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back_morfotype')],
    [InlineKeyboardButton(text='Начать тест', callback_data='start_morfotype')]])

start_morfotype = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Как провести измерения?', callback_data='chest_help')],
    [InlineKeyboardButton(text='Начать тест', callback_data='start_morfotype')]])

again_morfotype = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пройти заново', callback_data='morfotype')]])