from aiogram import F, Router, types

from database.msg import REPLIES
from keyboards.keyboards import get_funcs_keyboard
from scripts.decorators import member_required, spam_checker

router = Router()


@router.message(F)
@member_required
@spam_checker
async def cmd_incorrect(message: types.Message):
    await message.reply(REPLIES["INCORRECT"], reply_markup=get_funcs_keyboard())