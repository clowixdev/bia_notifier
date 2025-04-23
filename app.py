import asyncio

from handlers import start
from loader import bot, dp


async def main():
    dp.include_router(start.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot has been launched...")
    asyncio.run(main())