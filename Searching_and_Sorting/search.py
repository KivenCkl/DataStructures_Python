
def binary_search(sorted_seq, val):
    """实现标准库中的bisect.bisect_left
    """
    low = 0
    high = len(sorted_seq) - 1
    while low <= high:
        mid = (high + low) // 2
        if sorted_seq[mid] == val:
            return mid
        elif val < sorted_seq[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1   # 不存在该值

def test_sort():
    seq = [1, 5, 6, 8, 11, 15]
    assert binary_search(seq, 9) == -1
    assert binary_search(seq, 8) == 3

if __name__ == '__main__':
    test_sort()