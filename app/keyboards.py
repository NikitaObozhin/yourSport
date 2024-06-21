from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Показатели'),
                                      KeyboardButton(text='Рекомендации')],
                                      [KeyboardButton(text='О боте')]], 
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню')

parameters = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Морфотип', callback_data='morfotype')], 
    [InlineKeyboardButton(text='Психотип', callback_data='psychotype')]])
