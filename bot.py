import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import message_router

# Загрузка переменных  окружения из файла .env
load_dotenv()

async def main():
    bot = Bot(
        token=os.getenv("BOT_TOKEN"),
        parse_mode="HTML"
    )
    await bot.delete_webhook(drop_pending_updates=True)

    dp = Dispatcher()
    dp.include_router(message_router.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
