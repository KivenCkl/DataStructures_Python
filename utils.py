import time
from functools import wraps


def time_it(func):
    """
    计时装饰器
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        tmp = func(*args, **kwargs)
        print(f"{func.__name__} 运行时间：{time.time() - start}")
        return tmp

    return wrapper