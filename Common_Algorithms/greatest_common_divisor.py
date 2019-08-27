"""
greatest common divisor
最大公约数
"""
import random
import sys
sys.path.append("../")
from utils import time_it


@time_it
def gcd1(num1, num2):
    # 辗转相除法
    if num1 < num2:  # 调整大小顺序
        num1, num2 = num2, num1
    count = 1
    while num2 != 0:  # 辗转相除
        num1, num2 = num2, num1 % num2
        count += 1
    return [num1, count]


@time_it
def gcd2(num1, num2):
    # 更相减损术
    a = 1
    while (num1 % 2 == 0) and (num2 % 2 == 0):  # 均为偶数除2
        num1, num2 = num1 / 2, num2 / 2
        a *= 2
    count = 1
    while num2 != 0:  # 更相减损术
        if num1 < num2:  # 调整大小顺序
            num1, num2 = num2, num1
        num1, num2 = num2, num1 - num2
        count += 1
    return [num1 * a, count]


@time_it
def gcd3(num1, num2):
    # 除穷举法
    if num1 > num2:  # 取初始值
        a, b = num2, num1
    else:
        a, b = num1, num2
    count = 1
    a_0 = a
    while (b % a != 0):  # 穷举
        if a_0 % (count + 1) == 0:
            a = a_0 / (count + 1)
        count += 1
    return [a, count]


@time_it
def gcd4(num1, num2):
    # 减穷举法
    if num1 > num2:  # 取初始值
        a = num2
    else:
        a = num1
    count = 1
    while (num1 % a != 0) | (num2 % a != 0):  # 穷举
        a -= 1
        count += 1
        if count >= 1e6:
            a = 0
            break
    return [a, count]


if __name__ == '__main__':
    rg = 1E8
    a = random.randrange(rg)
    b = random.randrange(rg)
    g1 = gcd1(a, b)
    g2 = gcd2(a, b)
    g3 = gcd3(a, b)
    g4 = gcd4(a, b)
    print(f'GCD of ({a}, {b}):')
    print(f'辗转相除法: {g1[0]} ({g1[1]}次)')
    print(f'更相减损术: {g1[0]} ({g1[1]}次)')
    print(f'除穷举法: {g1[0]} ({g1[1]}次)')
    print(f'减穷举法: {g1[0]} ({g1[1]}次)')
