def binary_search(sorted_seq, val):
    """
    实现标准库中的 bisect.bisect_left
    """
    low = 0
    high = len(sorted_seq) - 1
    while low <= high:
        mid = (high + low) // 2
        if sorted_seq[mid] == val:
            return mid
        elif val <sorted_seq[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # 不存在该值


def bsearch_First(sorted_seq, val):
    """
    二分查找第一个值等于给定值的元素
    """
    low = 0
    high = len(sorted_seq) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if sorted_seq[mid] > val:
            high = mid - 1
        elif sorted_seq[mid] < val:
            low = mid + 1
        else:
            if mid == 0 or sorted_seq[mid - 1] != val:
                return mid
            else:
                high = mid - 1
    return -1


def bsearch_Last(sorted_seq, val):
    """
    二分查找最后一个值等于给定值的元素
    """
    low = 0
    high = len(sorted_seq) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if sorted_seq[mid] > val:
            high = mid - 1
        elif sorted_seq[mid] < val:
            low = mid + 1
        else:
            if mid == len(sorted_seq) - 1 or sorted_seq[mid + 1] != val:
                return mid
            else:
                low = mid + 1
    return -1


def bsearch_FirstLargerEqual(sorted_seq, val):
    """
    二分查找第一个大于等于给定值的元素
    """
    low = 0
    high = len(sorted_seq) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if sorted_seq[mid] >= val:
            if mid == 0 or sorted_seq[mid - 1] < val:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1


def bsearch_LastSmallerEqual(sorted_seq, val):
    """
    二分查找最后一个小于等于给定值的元素
    """
    low = 0
    high = len(sorted_seq) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if sorted_seq[mid] <= val:
            if mid == len(sorted_seq) - 1 or sorted_seq[mid + 1] > val:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -1


def bsearch_Circle(seq, val):
    """
    二分查找循环有序数组等于给定值的元素
    """
    low = 0
    high = len(seq) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if seq[mid] == val:
            return mid
        # 前半部分有序
        elif seq[low] < seq[mid]:
            # 所求值在有序部分
            if seq[low] <= val < seq[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # 后半部有序
        else:
            if seq[mid] < val <= seq[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def test_sort():
    seq = [1, 5, 6, 8, 11, 15]
    assert binary_search(seq, 9) == -1
    assert binary_search(seq, 8) == 3
    sorted_seq = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
    assert bsearch_First(sorted_seq, 8) == 5
    assert bsearch_Last(sorted_seq, 8) == 7
    assert bsearch_FirstLargerEqual(sorted_seq, 7) == 5
    assert bsearch_LastSmallerEqual(sorted_seq, 18) == 9
    seq = [4, 5, 6, 1, 2, 3]
    assert bsearch_Circle(seq, 1) == 3


if __name__ == '__main__':
    test_sort()