from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database.msg import REPLIES
from loader import engine
from database.dbworker import (get_user, 
                            turn_noti_on, 
                            turn_noti_off,
                            turn_dayinfo_on, 
                            turn_dayinfo_off,
                            turn_visibility_off,
                            turn_visibility_on,
                            set_dayinfo_time,
                            set_remind_time,
                            update_user_weekends)
from keyboards.keyboards import buttons
from keyboards.keyboards import (get_noti_off_keyboard, 
                                get_noti_on_keyboard, 
                                get_funcs_keyboard, 
                                get_back_only_keyboard, 
                                get_visibility_setting_keyboard,
                                get_dayinfo_setting_keyboard,
                                get_weekends_setting_keyboard)
from scripts.decorators import member_required, console_logging, spam_checker, chat_required
from states.states import Position
from scripts.functions import parse_from_weekends, is_time_correct

router = Router()


@router.message(Command("settings"))
@router.message(F.text == buttons["settings"])
@member_required
@spam_checker
@chat_required
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
@chat_required
@console_logging
async def cmd_settings_turn_on_noti(message: types.Message, state: FSMContext):
    turn_noti_on(message.from_user.id, engine)
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["TURN_NOTI_ON"])
    await message.reply(REPLIES["NOTI_ON"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))


@router.message(F.text == buttons["turn_off_noti"])
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_settings_turn_off_noti(message: types.Message, state: FSMContext):
    turn_noti_off(message.from_user.id, engine)
    turn_dayinfo_off(message.from_user.id, engine)
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["TURN_NOTI_OFF"])
    await message.reply(REPLIES["NOTI_OFF"], reply_markup=get_noti_off_keyboard())


@router.message(F.text == buttons["noti_remind"])
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_settings_remind(message: types.Message, state: FSMContext):
    await state.set_state(Position.remind_setting)
    await message.reply(REPLIES["NOTI_REMIND_SETUP"], reply_markup=get_back_only_keyboard())


@router.message(F.text == buttons["noti_dayinfo_setup"])
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_settings_dayinfo(message: types.Message, state: FSMContext):
    await state.set_state(Position.dayinfo_setting)
    await message.reply(REPLIES["NOTI_DAYINFO_SETUP"], reply_markup=get_dayinfo_setting_keyboard())


@router.message(F.text == buttons["noti_weekends"])
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_settings_weekends(message: types.Message, state: FSMContext):
    await state.set_state(Position.weekends_setting)
    await state.update_data(weekends=get_user(message.from_user.id, engine).noti_weekends)
    await message.reply(REPLIES["NOTI_WEEKENDS"].format(
        weekends="\n".join(parse_from_weekends(get_user(message.from_user.id, engine).noti_weekends))
    ), reply_markup=get_weekends_setting_keyboard())


@router.message(F.text == buttons["noti_visibility"])
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_settings_visibility(message: types.Message, state: FSMContext):
    await state.set_state(Position.visibility_setting) 
    await message.reply(REPLIES["NOTI_VISIBILITY"], reply_markup=get_visibility_setting_keyboard())


@router.message(F.text == buttons["noti_dayinfo_turn_on"])
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_settings_turn_on_dayinfo(message: types.Message, state: FSMContext):
    turn_dayinfo_on(message.from_user.id, engine)
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["NOTI_DAYINFO_TURNED_ON"])
    await message.reply(REPLIES["NOTI_ON"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))


@router.message(F.text == buttons["noti_dayinfo_turn_off"])
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_settings_turn_off_dayinfo(message: types.Message, state: FSMContext):
    turn_dayinfo_off(message.from_user.id, engine)
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["NOTI_DAYINFO_TURNED_OFF"])
    await message.reply(REPLIES["NOTI_ON"], reply_markup=get_noti_on_keyboard(0))


@router.message(Position.visibility_setting)
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_settings_visibility_validation(message: types.Message, state: FSMContext):
    if (message.text != buttons["visible"] and message.text != buttons["invisible"]):
        return
    else:
        if (message.text == buttons["visible"]):
            turn_visibility_on(message.from_user.id, engine)
        else:
            turn_visibility_off(message.from_user.id, engine)
        await state.set_state(Position.noti_on_settings)
        await message.reply(REPLIES["NOTI_VISIBILITY_VALIDATION"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))


@router.message(Position.weekends_setting)
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_settings_weekends_validation(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    if message.text == buttons["monday"]:
        if "1" not in user_data["weekends"]:
            await state.update_data(weekends=user_data["weekends"] + "1")
            await message.reply(REPLIES["MONDAY_ADDED"])
        else:
            await state.update_data(weekends=user_data["weekends"].replace("1", ""))
            await message.reply(REPLIES["MONDAY_REMOVED"])
    elif (message.text == buttons["tuesday"]):
        if "2" not in user_data["weekends"]:
            await state.update_data(weekends=user_data["weekends"] + "2")
            await message.reply(REPLIES["TUESDAY_ADDED"])
        else:
            await state.update_data(weekends=user_data["weekends"].replace("2", ""))
            await message.reply(REPLIES["TUESDAY_REMOVED"])
    elif (message.text == buttons["wednesday"]):
        if "3" not in user_data["weekends"]:
            await state.update_data(weekends=user_data["weekends"] + "3")
            await message.reply(REPLIES["WEDNESDAY_ADDED"])
        else:
            await state.update_data(weekends=user_data["weekends"].replace("3", ""))
            await message.reply(REPLIES["WEDNESDAY_REMOVED"])
    elif (message.text == buttons["thursday"]):
        if "4" not in user_data["weekends"]:
            await state.update_data(weekends=user_data["weekends"] + "4")
            await message.reply(REPLIES["THURSDAY_ADDED"])
        else:
            await state.update_data(weekends=user_data["weekends"].replace("4", ""))
            await message.reply(REPLIES["THURSDAY_REMOVED"])
    elif (message.text == buttons["friday"]):
        if "5" not in user_data["weekends"]:
            await state.update_data(weekends=user_data["weekends"] + "5")
            await message.reply(REPLIES["FRIDAY_ADDED"])
        else:
            await state.update_data(weekends=user_data["weekends"].replace("5", ""))
            await message.reply(REPLIES["FRIDAY_REMOVED"])
    elif (message.text == buttons["saturday"]):
        if "6" not in user_data["weekends"]:
            await state.update_data(weekends=user_data["weekends"] + "6")
            await message.reply(REPLIES["SATURDAY_ADDED"])
        else:
            await state.update_data(weekends=user_data["weekends"].replace("6", ""))
            await message.reply(REPLIES["SATURDAY_REMOVED"])
    elif (message.text == buttons["back_to_menu"]):
        await state.set_state(Position.noti_on_settings)
        print("DATA:", user_data["weekends"])
        update_user_weekends(message.from_user.id, engine, "".join([day for day in user_data["weekends"] if day != "0"]))
        await message.reply(REPLIES["NOTI_WEEKENDS_VALIDATION"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))
    else:
        await message.reply("Это не день недели", reply_markup=get_weekends_setting_keyboard())


@router.message(Command("back"))
@router.message(F.text == buttons["back_to_menu"])
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_back(message: types.Message, state: FSMContext):
    if (await state.get_state() == Position.noti_off_settings or \
        await state.get_state() == Position.noti_on_settings or \
        await state.get_state() == Position.contact or \
        await state.get_state() == None):
        
        await state.set_state(Position.main_menu)
        await message.reply(REPLIES["FUNCS"], reply_markup=get_funcs_keyboard())
    elif (await state.get_state() == Position.remind_setting or \
        await state.get_state() == Position.dayinfo_setting or \
        await state.get_state() == Position.weekends_setting or \
        await state.get_state() == Position.visibility_setting):
        
        await state.set_state(Position.noti_on_settings)
        await message.reply(REPLIES["NOTI_ON"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))


@router.message(Position.dayinfo_setting)
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_settings_dayinfo_validation(message: types.Message, state: FSMContext):
    dayinfo_time = is_time_correct(message.text)
    if (dayinfo_time == None):
        await message.reply(REPLIES["NOTI_DAYINFO_RETRY"], reply_markup=get_dayinfo_setting_keyboard())
        await message.reply(REPLIES["NOTI_DAYINFO_SETUP"], reply_markup=get_dayinfo_setting_keyboard())

        return
    await state.set_state(Position.noti_on_settings)
    set_dayinfo_time(message.from_user.id, engine, dayinfo_time)
    await message.reply(REPLIES["NOTI_DAYINFO_VALIDATION"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))


@router.message(Position.remind_setting)
@member_required
@spam_checker
@chat_required
@console_logging
async def cmd_settings_remind_validation(message: types.Message, state: FSMContext):
    remind_time = is_time_correct(message.text)
    if (remind_time == None):
        await message.reply(REPLIES["NOTI_REMIND_RETRY"], reply_markup=get_back_only_keyboard())
        await message.reply(REPLIES["NOTI_REMIND_SETUP"], reply_markup=get_back_only_keyboard())

        return
    await state.set_state(Position.noti_on_settings)
    set_remind_time(message.from_user.id, engine, remind_time)
    await state.set_state(Position.noti_on_settings)
    await message.reply(REPLIES["NOTI_REMIND_VALIDATION"], reply_markup=get_noti_on_keyboard(get_user(message.from_user.id, engine).noti_dayinfo))