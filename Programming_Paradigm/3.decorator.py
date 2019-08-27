"""
Decorator
装饰器模式

- 表面上看，装饰器模式就是扩展现有的一个函数的功能，让它可以干一些其他的事，或是在现有的函数功能上再附加上一些别的功能
- 除了可以感受到函数式编程下的代码扩展能力，还能感受到函数的互相和随意拼装带来的好处
- 装饰器几乎可以装饰所有的函数，因此，这种可以通用于其他函数的编程方式，可以很容易的将一些非业务功能的、属于控制类型的代码抽象出来（所谓的控制类型的代码就是像 for-loop，或是打日志，或是函数路由，或是求函数运行时间之类的非业务功能性的代码）
"""
from functools import wraps


def memorization(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        result = cache.get(*args)
        if result is None:
            result = func(*args)
            cache[args] = result
        return result

    return wrapper


@memorization
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    for i in range(10):
        print(fib(i))
