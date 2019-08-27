"""
全排列算法
"""


def permute(arr):
    """
    时间复杂度: O(n!)
    """
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        yield arr
    for i in range(len(arr)):
        x = arr[i]
        xs = arr[:i] + arr[i + 1:]
        for j in permute(xs):
            yield [x] + j


print(list(permute(list(range(4)))))
