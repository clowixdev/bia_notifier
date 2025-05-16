from typing import Union
from datetime import datetime

from keyboards.keyboards import buttons


def parse_from_weekends(weekends_str: str):
    weekends = []
    for day in weekends_str:
        match day:
            case "0":
                return weekends
            case "1":
                weekends.append(buttons["monday"])
            case "2":
                weekends.append(buttons["tuesday"])
            case "3":
                weekends.append(buttons["wednesday"])
            case "4":
                weekends.append(buttons["thursday"])
            case "5":
                weekends.append(buttons["friday"])
            case "6":
                weekends.append(buttons["saturday"])
            case _:
                print("Error occured while parsing weekends")
                break

    return weekends


def is_time_correct(message: str) -> Union[int, None]:
    try:
        if (datetime.strptime(message, "%H:%M")):
            return int("".join([char for char in message if char.isdigit()]))
    except ValueError:
        return None


def parse_from_dayinfo(time_int: int) -> str:
    clock_emoji = ""
    if (time_int < 100):
        h_part = "0"
        m_part = str(time_int)
    elif (time_int < 1000):
        h_part = str(time_int)[0]
        m_part = str(time_int)[1:]
    else:
        h_part = str(time_int)[:2]
        m_part = str(time_int)[2:]

    time = f"{h_part}:{"30" if (time_int % 100 - (time_int % 100 % 30)) / 30 else "00"}"
    if (time == "0:00" or time == "12:00"): clock_emoji =  "🕛"
    if (time == "1:00" or time == "13:00"): clock_emoji =  "🕐"
    if (time == "1:30" or time == "13:30"): clock_emoji =  "🕜"
    if (time == "0:30" or time == "12:30"): clock_emoji =  "🕧"
    if (time == "2:00" or time == "14:00"): clock_emoji =  "🕑"
    if (time == "2:30" or time == "14:30"): clock_emoji =  "🕝"
    if (time == "3:00" or time == "15:00"): clock_emoji =  "🕒"
    if (time == "3:30" or time == "15:30"): clock_emoji =  "🕞"
    if (time == "4:00" or time == "16:00"): clock_emoji =  "🕓"
    if (time == "4:30" or time == "16:30"): clock_emoji =  "🕟"
    if (time == "5:00" or time == "17:00"): clock_emoji =  "🕔"
    if (time == "5:30" or time == "17:30"): clock_emoji =  "🕠"
    if (time == "6:00" or time == "18:00"): clock_emoji =  "🕕"
    if (time == "6:30" or time == "18:30"): clock_emoji =  "🕡"
    if (time == "7:00" or time == "19:00"): clock_emoji =  "🕖"
    if (time == "7:30" or time == "19:30"): clock_emoji =  "🕢"
    if (time == "8:00" or time == "20:00"): clock_emoji =  "🕗"
    if (time == "8:30" or time == "20:30"): clock_emoji =  "🕣"
    if (time == "9:00" or time == "21:00"): clock_emoji =  "🕘"
    if (time == "9:30" or time == "21:30"): clock_emoji =  "🕤"
    if (time == "10:00" or time == "22:00"): clock_emoji =  "🕙"
    if (time == "10:30" or time == "22:30"): clock_emoji =  "🕥"
    if (time == "11:00" or time == "23:00"): clock_emoji =  "🕚"
    if (time == "11:30" or time == "23:30"): clock_emoji =  "🕦"

    return f"{h_part}:{m_part} {clock_emoji}"


def parse_from_remind(time_int: int) -> str:
    if (time_int < 100):
        h_part = "0"
        m_part = str(time_int)
    elif (time_int < 1000):
        h_part = str(time_int)[0]
        m_part = str(time_int)[1:]
    else:
        h_part = str(time_int)[:2]
        m_part = str(time_int)[2:]

    if (h_part != "0" and m_part != "00"):
        return f"за {h_part} ч. {m_part} мин."
    elif (m_part == "00"):
        return f"за {h_part} ч."
    else:
        return f"за {m_part} мин."