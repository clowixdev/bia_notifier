from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from database.msg import REPLIES
from keyboards.keyboards import buttons
from keyboards.keyboards import get_funcs_keyboard
from scripts.decorators import member_required
from states.states import Position

router = Router()


@router.message(Command("get"))
@router.message(F.text == buttons["get"])
@member_required
async def cmd_get(message: types.Message, state: FSMContext):
    await state.set_state(Position.main_menu)
    await message.reply(REPLIES["GET"], reply_markup=get_funcs_keyboard())