from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


morfotype = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Астенический', callback_data='asten')], 
    [InlineKeyboardButton(text='Нормостенический', callback_data='normosten')],
    [InlineKeyboardButton(text='Гиперстенический', callback_data='hypersten')],
    [InlineKeyboardButton(text='Рассчитать показатели', callback_data='parameters')],
    ])

psychotype = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Холерик', callback_data='holer')], 
    [InlineKeyboardButton(text='Флегматик', callback_data='fleg')],
    [InlineKeyboardButton(text='Сангвиник', callback_data='sang')],
    [InlineKeyboardButton(text='Меланхолик', callback_data='melan')],
    [InlineKeyboardButton(text='Рассчитать показатели', callback_data='parameters')],
    ])