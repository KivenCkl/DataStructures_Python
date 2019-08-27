"""
卡特兰数

卡特兰数又称卡塔兰数，英文名 Catalan number，是组合数学中一个常出现在各种计数问题中出现的数列。以比利时的数学家欧仁 · 查理 · 卡塔兰 (1814–1894) 的名字来命名，其前几项为 : 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790......

其递推公式为：
f(n)= f(0)*f(n-1)+f(1)*f(n-2)+...+f(n-1)*f(0) (n>=2)
例如：f(2)=f(0)*f(1)+f(1)*f(0)=1*1+1*1=2
f(3)=f(0)*f(2)+f(1)*f(1)+f(2)*f(0)=1*2+1*1+2*1=5

卡特兰数的应用

1、 n对括号正确匹配数目
给定n对括号，求括号正确配对的字符串数，例如：
0对括号：[空序列] 1种可能
1对括号：() 1种可能
2对括号：()() (()) 2种可能
3对括号：((())) ()(()) ()()() (())() (()()) 5种可能

2、凸多边形的三角划分
在一个凸多边形中，通过若干条互不相交的对角线，把这个多边形划分成了若干个三角形。任务是输入凸多边形的边数n，输出不同划分的方案数f(n)
n=0,1,2，均不能组成多边形，故而f(0)=f(1)=f(2)=0
n=3, 本身就是三角形，无需划分，故而f(3)=1
n=4, 考虑矩形，正反对角线，显然f(4)=2
n=5，五边形，一共五种，f(5)=5
n=6， 六边形，一共14种，f(6)=14

3、给定节点组成二叉搜索树
给定N个节点，能构成多少种不同的二叉搜索树？
n=0，规定空树也是一颗BST，故f(0)=1
n=1，显然f(1)=1
n=2，f(2)=2
n=3，f(3)=5
"""
import sys
sys.path.append("../")
from utils import time_it


@time_it
def catalan_1(n):
    # 暴力搜索法
    # O(2^N)
    if n <= 1:
        return 1
    total = 0
    for i in range(n):
        total += catalan_1(i) * catalan_1(n - 1 - i)
    return total


@time_it
def catalan_2(n):
    # 记忆搜索法
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    def dfs(n, dp):
        if dp[n] != 0:
            return dp[n]
        total = 0
        for i in range(n):
            total += dfs(i, dp) * dfs(n - 1 - i, dp)
        dp[n] = total
        return dp[n]

    return dfs(n, dp)


@time_it
def catalan_3(n):
    # 动态规划法
    # O(N^2)
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        total = 0
        for j in range(i):
            total += dp[j] * dp[i - 1 - j]
        dp[i] = total
    return dp[-1]


@time_it
def catalan_4(n):
    # 状态压缩法
    # O(N)
    if n <= 1:
        return 1
    a = 1
    for i in range(2, n + 1):
        b = a * (((i << 2) - 2) / (i + 1))
        a = b
    return int(a)


if __name__ == "__main__":
    # n = int(input())
    n = 8
    # if n < 10:
    #     print("暴力搜索法:", catalan_1(n))
    print("记忆搜索法:", catalan_2(n))
    print("动态规划法:", catalan_3(n))
    print("状态压缩法:", catalan_4(n))
