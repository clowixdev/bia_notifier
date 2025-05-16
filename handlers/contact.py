from aiogram import F, Router, types, Bot
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from database.msg import REPLIES
from keyboards.keyboards import buttons
from keyboards.keyboards import get_back_only_keyboard, get_funcs_keyboard
from scripts.decorators import member_required, console_logging, spam_checker, chat_required
from states.states import Position

from loader import support_chat_id, uptime_tickets

router = Router()


@router.message(Command("contact"))
@router.message(F.text == buttons["contact"])
@chat_required
@member_required
@spam_checker
@console_logging
async def cmd_contact(message: types.Message, state: FSMContext):
    await state.set_state(Position.contact)
    await message.reply(REPLIES["CONTACT"], reply_markup=get_back_only_keyboard())


@router.message(Position.contact)
@chat_required
@member_required
@spam_checker
@console_logging
async def messaging_contact(message: types.Message, state: FSMContext, bot: Bot):
    global uptime_tickets
    uptime_tickets += 1

    await state.set_state(Position.main_menu)
    await bot.send_message(support_chat_id, REPLIES["TICKET"].format(
        number=uptime_tickets, 
        ticket=message.text,
        user=message.from_user.username,
        date=message.date
        ))
    await message.reply(REPLIES["TICKET_SENT"], reply_markup=get_funcs_keyboard())