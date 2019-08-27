"""
Fibonacci sequence
斐波那契数列

F0 = 0                  (n=0)
F1 = 1                  (n=1)
Fn = F[n-1]+ F[n-2]     (n=>2)
"""
import numpy as np


def fib_1(n):
    # 递归
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_1(n - 1) + fib_1(n - 2)


def fib_2(n):
    # 循环
    res = []
    a, b = 0, 1
    while n > 0:
        res.append(b)
        a, b = b, a + b
        n -= 1
    return res


def fib_3(n):
    # yield 关键字
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


def fib_4(n):
    # 矩阵求解
    m = np.matrix('1 1; 1 0')
    return pow(m, n)


if __name__ == "__main__":
    print(fib_2(10))
    print(list(fib_3(10)))
    res = []
    for i in range(10):
        res.append(np.array(fib_4(i))[0][0])
    print(res)
