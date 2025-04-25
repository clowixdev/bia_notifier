from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from database.msg import REPLIES
from database.dbworker import add_user, get_user
from keyboards.keyboards import buttons
from keyboards.keyboards import get_funcs_keyboard
from scripts.decorators import member_required, console_logging, spam_checker
from states.states import Position

from loader import engine

router = Router()


@router.message(Command("start"))
@console_logging
@spam_checker
async def cmd_start(message: types.Message, state: FSMContext):
    if (get_user(message.from_user.id, engine) is None):
        add_user([
            message.from_user.id,
            0,
            0,
            0,
            0,
            0
        ], engine)

    await state.set_state(Position.main_menu)
    await message.reply(REPLIES["START"], reply_markup=get_funcs_keyboard())


@router.message(Command("help"))
@router.message(F.text == buttons["help"])
@member_required
@spam_checker
@console_logging
async def cmd_help(message: types.Message, state: FSMContext):
    await state.set_state(Position.main_menu)
    await message.reply(REPLIES["HELP"], reply_markup=get_funcs_keyboard())