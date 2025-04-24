from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from database.msg import REPLIES
from loader import engine
from database.dbworker import get_user
from keyboards.keyboards import buttons
from keyboards.keyboards import get_noti_off_keyboard, get_noti_on_keyboard, get_funcs_keyboard, get_back_only_keyboard, get_visibility_setting_keyboard
from scripts.decorators import member_required
from states.states import Position

router = Router()


@router.message(Command("settings"))
@router.message(F.text == buttons["settings"])
@member_required
async def cmd_settings(message: types.Message, state: FSMContext):
    user = get_user(message.from_user.id, engine)
    if (user.noti_status == True):
        await state.set_state(Position.noti_on_settings) 
        await message.reply(REPLIES["NOTI_ON"], reply_markup=get_noti_on_keyboard())
    else:
        await state.set_state(Position.noti_off_settings)
        await message.reply(REPLIES["NOTI_OFF"], reply_markup=get_noti_off_keyboard())


@router.message(F.text == buttons["noti_frequency"])
@member_required
async def cmd_settings_freq(message: types.Message, state: FSMContext):
    await state.set_state(Position.frequency_setting)
    await message.reply(REPLIES["NOTI_FREQ"], reply_markup=get_back_only_keyboard())


@router.message(F.text == buttons["noti_amount"])
@member_required
async def cmd_settings_amount(message: types.Message, state: FSMContext):
    await state.set_state(Position.amount_setting) 
    await message.reply(REPLIES["NOTI_AMT"], reply_markup=get_back_only_keyboard())


@router.message(F.text == buttons["noti_weekends"])
@member_required
async def cmd_settings_weekends(message: types.Message, state: FSMContext):
    await state.set_state(Position.weekends_setting) 
    await message.reply(REPLIES["NOTI_WEEKENDS"], reply_markup=get_back_only_keyboard())


@router.message(F.text == buttons["noti_visibility"])
@member_required
async def cmd_settings_visibility(message: types.Message, state: FSMContext):
    await state.set_state(Position.visibility_setting) 
    await message.reply(REPLIES["NOTI_VISIBILITY"], reply_markup=get_visibility_setting_keyboard())


@router.message(F.text == buttons["turn_on_noti"])
@member_required
async def cmd_settings_visibility(message: types.Message, state: FSMContext):
    # change noti state for user
    await state.set_state(Position.noti_on_settings) 
    await message.reply(REPLIES["NOTI_ON"])
    await message.reply(REPLIES["TURN_NOTI_ON"], reply_markup=get_noti_on_keyboard())


@router.message(Command("back"))
@router.message(F.text == buttons["back_to_menu"])
@member_required
async def cmd_back(message: types.Message, state: FSMContext):
    if (await state.get_state() == Position.noti_off_settings or \
        await state.get_state() == Position.noti_on_settings):
        
        await state.set_state(Position.main_menu)
        await message.reply(REPLIES["FUNCS"], reply_markup=get_funcs_keyboard())
    
    elif (await state.get_state() == Position.frequency_setting or \
        await state.get_state() == Position.amount_setting or \
        await state.get_state() == Position.weekends_setting or \
        await state.get_state() == Position.visibility_setting):
        
        await state.set_state(Position.noti_on_settings)
        await message.reply(REPLIES["NOTI_ON"], reply_markup=get_noti_on_keyboard())


@router.message(Position.visibility_setting)
@member_required
async def cmd_settings_visibility_validation(message: types.Message, state: FSMContext):
    # input_validation
    await state.set_state(Position.noti_on_settings) 
    await message.reply(REPLIES["NOTI_VISIBILITY_VALIDATION"], reply_markup=get_noti_on_keyboard())


@router.message(Position.weekends_setting)
@member_required
async def cmd_settings_weekends_validation(message: types.Message, state: FSMContext):
    # input validation
    await state.set_state(Position.noti_on_settings) 
    await message.reply(REPLIES["NOTI_WEEKENDS_VALIDATION"], reply_markup=get_noti_on_keyboard())


@router.message(Position.amount_setting)
@member_required
async def cmd_settings_amount_validation(message: types.Message, state: FSMContext):
    # input validation
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["NOTI_AMT_VALIDATION"], reply_markup=get_noti_on_keyboard())


@router.message(Position.frequency_setting)
@member_required
async def cmd_settings_freq_validation(message: types.Message, state: FSMContext):
    # input validation
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["NOTI_FREQ_VALIDATION"], reply_markup=get_noti_on_keyboard())