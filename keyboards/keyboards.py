from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_start_keyboard():
    kb_list = [
        [KeyboardButton(text="📖 Старт"), KeyboardButton(text="👤 Помощь")]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Воспользуйтесь меню:"
    )

    return keyboard