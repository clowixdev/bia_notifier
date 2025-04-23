from os import environ

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from database.dbworker import create_db_engine

load_dotenv(".env")

bot = Bot(
    token=environ.get("TOKEN"),
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

engine = create_db_engine()
dp = Dispatcher(storage=MemoryStorage())