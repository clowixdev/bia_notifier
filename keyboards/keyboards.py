from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons = {
    "get": "📆 Получить календарь",
    "settings": "⚙️ Настройки",
    "help": "ℹ️ Помощь",
    "noti_frequency": "🔔 Частота оповещений",
    "noti_amount": "🔢 Количество оповещений",
    "noti_weekends": "⛱️ Выходные дни",
    "noti_visibility": "👀 Видимость оповещений",
    "back_to_menu": "↩ Вернуться в главное меню",
    "turn_on_noti": "🔔 Включить и настроить оповещения",
    "placeholder": "📜 Воспользуйтесь меню:",
    "visible": "😄 Видимые",
    "invisible": "🫣 Невидимые"
}

def get_funcs_keyboard():
    kb_list = [
        [KeyboardButton(text=buttons["get"])],
        [KeyboardButton(text=buttons["settings"]), KeyboardButton(text=buttons["help"])]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder=buttons["placeholder"]
    )

    return keyboard


def get_noti_on_keyboard():
    kb_list = [
        [KeyboardButton(text=buttons["noti_frequency"]), KeyboardButton(text=buttons["noti_amount"])],
        [KeyboardButton(text=buttons["noti_weekends"]), KeyboardButton(text=buttons["noti_visibility"])],
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