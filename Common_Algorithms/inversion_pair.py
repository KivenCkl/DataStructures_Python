"""
inversion pair
逆序对

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对
"""


def inverse_pairs(data):
    """
    借助归并排序的分治思想，在每次合并的时候统计逆序对
    """
    if len(data) < 2:
        return 0
    mid = (len(data) + 1) // 2
    left_half = data[:mid]
    right_half = data[mid:]
    left_count = inverse_pairs(left_half) % 1000000007
    right_count = inverse_pairs(right_half) % 1000000007
    i, j, k, count = len(left_half) - 1, len(right_half) - 1, len(data) - 1, 0
    while i >= 0 and j >= 0:
        if left_half[i] < right_half[j]:
            data[k] = right_half[j]
            j = j - 1
            k = k - 1
        else:
            data[k] = left_half[i]
            count += (j + 1)
            i = i - 1
            k = k - 1
    while i >= 0:
        data[k] = left_half[i]
        k = k - 1
        i = i - 1
    while j >= 0:
        data[k] = right_half[j]
        k = k - 1
        j = j - 1
    return (count + left_count + right_count) % 1000000007


if __name__ == "__main__":
    # data = [11, 8, 3, 9, 7, 1, 2, 5]
    data = [1, 2, 3, 4, 5, 6, 0]
    print(inverse_pairs(data))
