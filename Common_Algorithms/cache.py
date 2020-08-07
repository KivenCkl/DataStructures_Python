"""
Cache

根据调用的函数名和调用的参数，对函数的结果进行缓存，下次执行的时候就不用重复计算

使用示例：
@cache()
def complex(a, b):
    time.sleep(2)
    return a + b
"""
import time
import hashlib
import pickle
from functools import wraps

cache = {}


def is_obsolete(entry, duration):
    d = time.time() - entry['time']
    return d > duration


def compute_key(function, args, kwargs):
    key = pickle.dumps((function.__name__, args, kwargs))
    return hashlib.sha1(key).hexdigest()


def cache(duration=10):
    def _decorate(function):
        @wraps(function)  # update_wrapper维持被修饰函数属性不变
        def __wrapper(*args, **kwargs):
            key = compute_key(function, args, kwargs)

            if key in cache and not is_obsolete(cache[key], duration):
                print('we got a winner')
                return cache[key]['value']

            result = function(*args, **kwargs)
            cache[key] = {'value': result, 'time': time.time()}
            return result

        return __wrapper

    return _decorate