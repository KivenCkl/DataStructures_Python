"""
1. A recursive solution must contain a base case;
2. A recursion solution must contain a recursive case;
3. A recursion solution must make progress toward the base case.
"""


def printRev(n):
    """ 倒序输出 n 到 1
    """
    if n > 0:
        print(n)
        printRev(n - 1)


def printInOrder(n):
    """ 正序输出 1 到 n
    """
    if n > 0:
        printInOrder(n - 1)
        print(n)


def recBinarySeacher(target, theSeq, first, last):
    """ 使用递归实现二分查找
    """
    if first > last:
        return False
    else:
        mid = (first + last) // 2
        if theSeq[mid] == target:
            return True
        elif theSeq[mid] > target:
            return recBinarySeacher(target, theSeq, first, mid - 1)
        else:
            return recBinarySeacher(target, theSeq, mid + 1, last)
