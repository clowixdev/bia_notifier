from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter

from database.msg import REPLIES
from database.dbworker import get_user
from keyboards.keyboards import buttons, get_funcs_keyboard
from scripts.decorators import member_required, console_logging
from loader import engine

router = Router()

@router.message(Command("my_info"))
@router.message(F.text == buttons["my_info"])
@member_required
@console_logging
async def cmd_myinfo(message: types.Message):
    user = get_user(message.from_user.id, engine)
    await message.reply(REPLIES["MY_INFO"].format(
        freq=user.noti_freq,
        weekends=user.noti_weekends,
        dayinfo=user.noti_dayinfo,
        visibility=user.noti_visibility
    ), reply_markup=get_funcs_keyboard())