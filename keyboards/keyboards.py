from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons = {
    "get": "📆 Получить календарь",
    "settings": "⚙️ Настройки",
    "help": "ℹ️ Помощь",
    "my_info": "🪪 Мой профиль",
    "noti_frequency": "🔔 Частота оповещений",
    "noti_dayinfo_turn_on": "📑 Включить повестку дня",
    "noti_dayinfo_turn_off": "💤 Выключить повестку дня",
    "noti_dayinfo_setup": "🕒 Настроить повестку дня",
    "noti_weekends": "⛱️ Выходные дни",
    "noti_visibility": "👀 Видимость оповещений",
    "back_to_menu": "↩ Вернуться в главное меню",
    "turn_on_noti": "🔔 Включить и настроить оповещения",
    "turn_off_noti": "🔕 Выключить оповещения",
    "placeholder": "📜 Воспользуйтесь меню:",
    "visible": "👓 Видимые",
    "invisible": "🕶️ Невидимые",
    "monday": "☕ Понедельник",
    "tuesday": "🥞 Вторник",
    "wednesday": "🔮 Среда",
    "thursday": "🏈 Четверг",
    "friday": "🍻 Пятница",
    "saturday": "🌆 Суббота"
}

def get_funcs_keyboard():
    kb_list = [
        [KeyboardButton(text=buttons["get"])],
        [KeyboardButton(text=buttons["my_info"])],
        [KeyboardButton(text=buttons["settings"]), KeyboardButton(text=buttons["help"])]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=buttons["placeholder"]
    )

    return keyboard


def get_noti_on_keyboard(dayinfo_state: int):
    kb_list = [
        [KeyboardButton(text=buttons["noti_frequency"]), KeyboardButton(
            text=buttons["noti_dayinfo_setup"] if dayinfo_state != 0 else buttons["noti_dayinfo_turn_on"]
            )],
        [KeyboardButton(text=buttons["noti_weekends"]), KeyboardButton(text=buttons["noti_visibility"])],
        [KeyboardButton(text=buttons["turn_off_noti"])],
        [KeyboardButton(text=buttons["back_to_menu"])]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=buttons["placeholder"]
    )

    return keyboard


def get_noti_off_keyboard():
    kb_list = [
        [KeyboardButton(text=buttons["turn_on_noti"])],
        [KeyboardButton(text=buttons["back_to_menu"])]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=buttons["placeholder"]
    )

    return keyboard


def get_visibility_setting_keyboard():
    kb_list = [
        [KeyboardButton(text=buttons["visible"]), KeyboardButton(text=buttons["invisible"])],
        [KeyboardButton(text=buttons["back_to_menu"])]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=buttons["placeholder"]
    )

    return keyboard


def get_dayinfo_setting_keyboard():
    kb_list = [
        [KeyboardButton(text=buttons["noti_dayinfo_turn_off"])],
        [KeyboardButton(text=buttons["back_to_menu"])]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=buttons["placeholder"]
    )

    return keyboard


def get_weekends_setting_keyboard():
    kb_list = [
        [KeyboardButton(text=buttons["monday"]), KeyboardButton(text=buttons["tuesday"]), KeyboardButton(text=buttons["wednesday"])],
        [KeyboardButton(text=buttons["thursday"]), KeyboardButton(text=buttons["friday"]), KeyboardButton(text=buttons["saturday"])],
        [KeyboardButton(text=buttons["back_to_menu"])]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=buttons["placeholder"]
    )

    return keyboard


def get_back_only_keyboard():
    kb_list = [
        [KeyboardButton(text=buttons["back_to_menu"])]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=buttons["placeholder"]
    )

    return keyboard