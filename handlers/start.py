from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from loader import engine
from database.msg import REPLIES
from keyboards.keyboards import get_start_keyboard

router = Router()


@router.message(Command("start"))
@router.message(F.text == "📖 Старт")
async def cmd_help(message: types.Message):
    await message.reply(REPLIES["START"], reply_markup=get_start_keyboard())


@router.message(Command("help"))
@router.message(F.text == "👤 Помощь")
async def cmd_help(message: types.Message):
    await message.reply(REPLIES["HELP"], reply_markup=get_start_keyboard())


@router.message(F)
async def cmd_help(message: types.Message):
    await message.reply(message.text, reply_markup=get_start_keyboard())