from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from database.msg import REPLIES
from loader import engine
from database.dbworker import get_user, turn_noti_on, turn_noti_off, turn_dayinfo_on, turn_dayinfo_off
from keyboards.keyboards import buttons
from keyboards.keyboards import (get_noti_off_keyboard, 
                                get_noti_on_keyboard, 
                                get_funcs_keyboard, 
                                get_back_only_keyboard, 
                                get_visibility_setting_keyboard,
                                get_dayinfo_setting_keyboard,
                                get_weekends_setting_keyboard)
from scripts.decorators import member_required, console_logging, spam_checker
from states.states import Position

router = Router()


@router.message(Command("settings"))
@router.message(F.text == buttons["settings"])
@member_required
@spam_checker
@console_logging
async def cmd_settings(message: types.Message, state: FSMContext):
    user = get_user(message.from_user.id, engine)
    if (user.noti_status == True):
        await state.set_state(Position.noti_on_settings) 
        await message.reply(REPLIES["NOTI_ON"], reply_markup=get_noti_on_keyboard(user.noti_dayinfo))
    else:
        await state.set_state(Position.noti_off_settings)
        await message.reply(REPLIES["NOTI_OFF"], reply_markup=get_noti_off_keyboard())


@router.message(F.text == buttons["turn_on_noti"])
@member_required
@spam_checker
@console_logging
async def cmd_settings_turn_on_noti(message: types.Message, state: FSMContext):
    turn_noti_on(message.from_user.id, engine)
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["TURN_NOTI_ON"])
    await message.reply(REPLIES["NOTI_ON"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))


@router.message(F.text == buttons["turn_off_noti"])
@member_required
@spam_checker
@console_logging
async def cmd_settings_turn_off_noti(message: types.Message, state: FSMContext):
    turn_noti_off(message.from_user.id, engine)
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["TURN_NOTI_OFF"])
    await message.reply(REPLIES["NOTI_OFF"], reply_markup=get_noti_off_keyboard())


@router.message(F.text == buttons["noti_frequency"])
@member_required
@spam_checker
@console_logging
async def cmd_settings_freq(message: types.Message, state: FSMContext):
    await state.set_state(Position.frequency_setting)
    await message.reply(REPLIES["NOTI_FREQ"], reply_markup=get_back_only_keyboard())


@router.message(F.text == buttons["noti_dayinfo_setup"])
@member_required
@spam_checker
@console_logging
async def cmd_settings_dayinfo(message: types.Message, state: FSMContext):
    await state.set_state(Position.dayinfo_setting)
    await message.reply(REPLIES["NOTI_DAYINFO_SETUP"], reply_markup=get_dayinfo_setting_keyboard())


@router.message(F.text == buttons["noti_weekends"])
@member_required
@spam_checker
@console_logging
async def cmd_settings_weekends(message: types.Message, state: FSMContext):
    await state.set_state(Position.weekends_setting) 
    await message.reply(REPLIES["NOTI_WEEKENDS"].format(weekends=get_user(message.from_user.id, engine).noti_weekends), 
                        reply_markup=get_weekends_setting_keyboard())


@router.message(F.text == buttons["noti_visibility"])
@member_required
@spam_checker
@console_logging
async def cmd_settings_visibility(message: types.Message, state: FSMContext):
    await state.set_state(Position.visibility_setting) 
    await message.reply(REPLIES["NOTI_VISIBILITY"], reply_markup=get_visibility_setting_keyboard())


@router.message(F.text == buttons["noti_dayinfo_turn_on"])
@member_required
@spam_checker
@console_logging
async def cmd_settings_turn_on_dayinfo(message: types.Message, state: FSMContext):
    turn_dayinfo_on(message.from_user.id, engine)
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["NOTI_DAYINFO_TURNED_ON"])
    await message.reply(REPLIES["NOTI_ON"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))


@router.message(F.text == buttons["noti_dayinfo_turn_off"])
@member_required
@spam_checker
@console_logging
async def cmd_settings_turn_off_dayinfo(message: types.Message, state: FSMContext):
    turn_dayinfo_off(message.from_user.id, engine)
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["NOTI_DAYINFO_TURNED_OFF"])
    await message.reply(REPLIES["NOTI_ON"], reply_markup=get_noti_on_keyboard(0))


@router.message(Command("back"))
@router.message(F.text == buttons["back_to_menu"])
@member_required
@spam_checker
@console_logging
async def cmd_back(message: types.Message, state: FSMContext):
    if (await state.get_state() == Position.noti_off_settings or \
        await state.get_state() == Position.noti_on_settings):
        
        await state.set_state(Position.main_menu)
        await message.reply(REPLIES["FUNCS"], reply_markup=get_funcs_keyboard())
    
    elif (await state.get_state() == Position.frequency_setting or \
        await state.get_state() == Position.dayinfo_setting or \
        await state.get_state() == Position.weekends_setting or \
        await state.get_state() == Position.visibility_setting):
        
        await state.set_state(Position.noti_on_settings)
        await message.reply(REPLIES["NOTI_ON"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))


@router.message(Position.visibility_setting)
@member_required
@spam_checker
@console_logging
async def cmd_settings_visibility_validation(message: types.Message, state: FSMContext):
    # input_validation
    await state.set_state(Position.noti_on_settings) 
    await message.reply(REPLIES["NOTI_VISIBILITY_VALIDATION"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))


@router.message(Position.weekends_setting)
@member_required
@spam_checker
@console_logging
async def cmd_settings_weekends_validation(message: types.Message, state: FSMContext):
    if message.text == buttons["monday"]:
        # add day
        await message.reply(REPLIES["MONDAY_ADDED"])
    elif (message.text == buttons["tuesday"]):
        # add day
        await message.reply(REPLIES["TUESDAY_ADDED"])
    elif (message.text == buttons["wednesday"]):
        # add day
        await message.reply(REPLIES["WEDNESDAY_ADDED"])
    elif (message.text == buttons["thursday"]):
        # add day
        await message.reply(REPLIES["THURSDAY_ADDED"])
    elif (message.text == buttons["friday"]):
        # add day
        await message.reply(REPLIES["FRIDAY_ADDED"])
    elif (message.text == buttons["saturday"]):
        # add day
        await message.reply(REPLIES["SATURDAY_ADDED"])
    elif (message.text == buttons["back"]):
        await state.set_state(Position.noti_on_settings)
        await message.reply(REPLIES["NOTI_WEEKENDS_VALIDATION"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))
    else:
        await message.reply("Это не день недели", reply_markup=get_weekends_setting_keyboard())


@router.message(Position.dayinfo_setting)
@member_required
@spam_checker
@console_logging
async def cmd_settings_dayinfo_validation(message: types.Message, state: FSMContext):
    # input validation
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["NOTI_DAYINFO_VALIDATION"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))


@router.message(Position.frequency_setting)
@member_required
@spam_checker
@console_logging
async def cmd_settings_freq_validation(message: types.Message, state: FSMContext):
    # input validation
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["NOTI_FREQ_VALIDATION"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))