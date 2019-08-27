"""
least common multiple
最小公倍数
"""
import random
from greatest_common_divisor import gcd1
import sys
sys.path.append("../")
from utils import time_it


@time_it
def lcm1(num1, num2):
    # GCD 法
    gcd = gcd1(num1, num2)
    a = num1 * num2 / gcd[0]
    return [a, gcd[1]]


@time_it
def lcm2(num1, num2):
    # 乘穷举法
    if num1 >= num2:  # 取初始值
        a = num1
    else:
        a = num2
    count = 1
    a_0 = a
    while (a % num1 != 0) | (a % num2 != 0):  # 穷举
        a = a_0 * (count + 1)
        count += 1
    return [a, count]


@time_it
def lcm3(num1, num2):
    # 加穷举法
    if num1 >= num2:  # 取初始值
        a = num1
    else:
        a = num2
    count = 1
    while (a % num1 != 0) | (a % num2 != 0):  # 穷举
        a += 1
        count += 1
        if count >= 1e6:
            a = 0
            break
    return [a, count]


if __name__ == '__main__':
    rg = 1E6
    a = random.randrange(rg)
    b = random.randrange(rg)
    g1 = lcm1(a, b)
    g2 = lcm2(a, b)
    g3 = lcm3(a, b)
    print(f'LCM of ({a}, {b}):')
    print(f'GCD法: {g1[0]} ({g1[1]}次)')
    print(f'乘穷举法: {g1[0]} ({g1[1]}次)')
    print(f'加穷举法: {g1[0]} ({g1[1]}次)')
