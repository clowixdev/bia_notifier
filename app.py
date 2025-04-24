import asyncio

from handlers import start, get, settings, incorrect
from loader import bot, dp


async def main():
    dp.include_router(start.router)
    dp.include_router(get.router)
    dp.include_router(settings.router)
    dp.include_router(incorrect.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot has been launched...")
    asyncio.run(main())