from typing import Callable, Any
from functools import wraps
from datetime import datetime
from time import time

from database.dbworker import get_user
from loader import engine, last_message

def spam_checker(func: Callable) -> Any:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if args[0].from_user.id not in last_message:
            last_message[args[0].from_user.id] = float(0)

        if (float(time()) - float(last_message[args[0].from_user.id])) < 0.5:
            return

        last_message[args[0].from_user.id] = float(time())
        return await func(*args, **kwargs)
    return wrapper


def member_required(func: Callable) -> Any:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if (get_user(args[0].from_user.id, engine) is None):
            return
        return await func(*args, **kwargs)
    return wrapper


def console_logging(func: Callable) -> Any:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print("{date} {user_id}:@{username} called {func_name}".format(
            date=datetime.now(),
            user_id=args[0].from_user.id,
            username=args[0].from_user.username,
            func_name=func.__name__
        ))
        return await func(*args, **kwargs)
    return wrapper