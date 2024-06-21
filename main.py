import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from app.handlers import mainRouter
from app.morfotype.handlers import morfotypeRouter
from app.psychotype.handlers import psychotypeRouter
from app.recomendations.handlers import recomendationsRouter


# основная функция для полинга сервера telegram
async def main():
    # Создание бота и деспетчера
    bot = Bot(token='token', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(mainRouter)
    dp.include_router(morfotypeRouter)
    dp.include_router(psychotypeRouter)
    dp.include_router(recomendationsRouter)
    await dp.start_polling(bot)


# безопасность от ошибки импорта
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Работа бота остановлена!')