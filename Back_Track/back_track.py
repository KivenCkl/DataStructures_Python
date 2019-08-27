"""
回溯算法

包括三类问题：
1. Find a path to success 是否有解
2. Find all paths to success 求所有解
    2.1 求所有解的个数
    2.2 求所有解的具体信息
3. Find the best path to success 求最优解

以八皇后 N-Queens 为例
"""


def is_valid(arr: list) -> bool:
    """
    用于判断最后一行是否和前面冲突
    """
    last_ind = len(arr) - 1
    last_col = arr[-1]
    for ind, col in arr[:-1]:
        if abs(ind - last_ind) == abs(col - last_col) or col == last_col:
            return False
    return True


def back_track_1(i: int, matrix: list, n: int) -> bool:
    """
    第 1 类问题
    一行一行的放 queen，每行尝试 n 个可能，有一个可达，返回 True
    都不可达，返回 False
    """
    if i == n:
        if is_valid(matrix):
            return True
        return False

    for j in range(n):
        matrix.append(j)
        if is_valid(matrix):  # 剪枝
            if back_track_1(i + 1, matrix, n):
                return True
        matrix.pop()
    return False


count = 0  # 全局变量


def back_track_2(i: int, matrix: list, n: int) -> None:
    """
    第 2.1 类问题
    一行一行的放 queen，每行尝试 n 个可能，因为需要找所有，因此不需要返回值
    在搜索时，如果有一个可达，仍要继续尝试，当每个子选项都试完了，返回
    """
    global count
    if i == n:
        if is_valid(matrix):
            count += 1
        return

    for j in range(n):
        matrix.append(j)
        if is_valid(matrix):  # 剪枝
            back_track_2(i + 1, matrix, n)
        matrix.pop()


result = []  # 全局变量


def back_track_3(i: int, matrix: list, n: int) -> None:
    """
    第 2.2 类问题
    一行一行的放 queen，每行尝试 n 个可能，因为需要找所有，因此不需要返回值
    在搜索时，如果有一个可达，仍要继续尝试，当每个子选项都试完了，返回
    """
    if i == n:
        if is_valid(matrix):
            result.append(matrix)
        return

    for j in range(n):
        matrix.append(j)
        if is_valid(matrix):  # 剪枝
            back_track_3(i + 1, matrix, n)
        matrix.pop()
