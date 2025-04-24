from aiogram.fsm.state import StatesGroup, State

class Position(StatesGroup):
    main_menu = State()

    noti_on_settings = State()
    noti_off_settings = State()
    
    frequency_setting = State()
    amount_setting = State()
    weekends_setting = State()
    visibility_setting = State()