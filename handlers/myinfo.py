from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter

from database.msg import REPLIES
from database.dbworker import get_user
from keyboards.keyboards import buttons, get_funcs_keyboard
from scripts.decorators import member_required, console_logging, chat_required
from scripts.functions import parse_from_weekends, parse_from_dayinfo, parse_from_remind
from loader import engine

router = Router()

@router.message(Command("my_info"))
@router.message(F.text == buttons["my_info"])
@chat_required
@member_required
@console_logging
async def cmd_myinfo(message: types.Message):
    user = get_user(message.from_user.id, engine)
    if user.noti_dayinfo == 0:
        dayinfo = REPLIES["DAYINFO_OFF"]
    elif user.noti_dayinfo == 1:
        dayinfo = REPLIES["DAYINFO_ON"]
    else:
        dayinfo = parse_from_dayinfo(user.noti_dayinfo)

    if user.noti_remind == 0:
        remind = REPLIES["REMIND_OFF"]
    else:
        remind = parse_from_remind(user.noti_remind)

    if user.noti_weekends == "0":
        weekends = REPLIES["WEEKENDS_OFF"]
    else:
        weekends = "\n\t\t\t" + "\n\t\t\t".join(parse_from_weekends(user.noti_weekends))

    if user.noti_status == 0:
        await message.reply(REPLIES["NOTI_OFF_MYINFO"], reply_markup=get_funcs_keyboard())
    else:
        await message.reply(REPLIES["MY_INFO"].format(
        remind=remind,
        weekends=weekends,
        dayinfo=dayinfo,
        visibility=buttons["visible"] if user.noti_visibility else buttons["invisible"]
    ), reply_markup=get_funcs_keyboard())