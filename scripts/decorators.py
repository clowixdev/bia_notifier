from typing import Callable, Any
from functools import wraps

from database.dbworker import get_user
from loader import engine

def member_required(func: Callable) -> Any:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print(args[0].from_user.id, args[0].from_user.username)
        if (get_user(args[0].from_user.id, engine) is None):
            return
        return await func(*args, **kwargs)
    return wrapper