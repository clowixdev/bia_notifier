from aiogram.fsm.state import StatesGroup, State

class Position(StatesGroup):
    main_menu = State()
    contact = State()

    noti_on_settings = State()
    noti_off_settings = State()
    
    remind_setting = State()
    dayinfo_setting = State()
    weekends_setting = State()
    visibility_setting = State()