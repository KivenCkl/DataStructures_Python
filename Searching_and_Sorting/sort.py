
def bubble_sort(seq):   # O(n^2)
    """冒泡排序
    """
    n = len(seq)
    if n <= 1:
        return
    for i in range(n-1):
        flag = False
        for j in range(n-1-i):
        # 每一轮冒泡最大的元素都会冒泡到最后，无须比较
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
                flag = True
        if not flag:
            break

def select_sort(seq):
    """选择排序
    可以看作是冒泡的改进，每次找一个最小的元素交换，每一轮只需要交换一次
    """
    n = len(seq)
    if n <= 1:
        return
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if seq[j] < seq[min_idx]:   # 找到最小元素的下标
                min_idx = j
        if min_idx != i:
            seq[i], seq[min_idx] = seq[min_idx], seq[i]

def insertion_sort(seq):
    """插入排序
    每次挑选下一个元素插入已经排序的数组中，初始时已排序数组只有一个元素
    """
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos-1]:
            # 将当前值插入至合适位置，其余元素后移
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value

"""
Advanced Sorting
"""

def merge_sorted_list(listA, listB):
    """归并两个有序数组，O(max(len(listA), len(listB)))
    """
    new_list = list()
    a = b = 0
    while a < len(listA) and b < len(listA):
        if listA[a] <= listB[b]:
            new_list.append(listA[a])
            a += 1
        else:
            new_list.append(listB[b])
            b += 1
    while a < len(listA):
        new_list.append(listA[a])
        a += 1
    while b < len(listB):
        new_list.append(listB[b])
        b += 1
    return new_list

def mergesort(theList):
    """归并排序，时间复杂度：O(nlogn)， 空间复杂度：O(n)
    mergesort: divided and conquer 分治算法
    1. 把原数组分解成越来越小的子数组
    2. 合并子数组来创建一个有序数组
    """
    if len(theList) <= 1:
        return theList
    else:
        mid = len(theList) // 2
        # 递归分解左右两边数组
        left_half = mergesort(theList[:mid])
        right_half = mergesort(theList[mid:])
        # 合并两边的有序子数组
        newList = merge_sorted_list(left_half, right_half)
        return newList

def quicksort(theSeq):
    """快速排序，average: O(nlogn)，原地算法
    quicksort: 也是分治，但是和归并排序不同的是，采用选定主元(pivot)而不是从中间进行数组划分
    1. 第一步选定pivot用来划分数组，pivot左边元素都比它小，右边元素都大于等于它
    2. 对划分的左右两边数组递归，直到递归出口（数组元素数目小于2）
    3. 对pivot和左右划分的数组合并成一个有序数组
    """
    length = len(theSeq)
    _quicksort(theSeq, 0, length-1)

def _quicksort(theSeq, first, last):
    if first < last:
        pos = partitionSeq(theSeq, first, last)
        # 对划分的子数组递归操作
        _quicksort(theSeq, first, pos-1)
        _quicksort(theSeq, pos+1, last)

def partitionSeq(theSeq, first, last):
    """快排中的划分操作
    把比pivot小的挪到左边，比pivot大的挪到右边
    """
    pivot = theSeq[last]
    i = first
    for j in range(first, last):
        if theSeq[j] < pivot:
            theSeq[i], theSeq[j] = theSeq[j], theSeq[i]
            i += 1
    theSeq[i], theSeq[last] = theSeq[last], theSeq[i]
    return i    # 返回pivot的位置

def nth_element(theSeq, K):
    """快速查找一个无序数组中的第K大元素
    """
    return _nth_element(theSeq, 0, len(theSeq)-1, K)

def _nth_element(theSeq, first, last, K):
    if len(theSeq) < K:
        raise Exception('The list only has %d numbers!' % len(theSeq))
    pivot_index = partitionSeq(theSeq, first, last)
    if len(theSeq)-pivot_index == K:
        return theSeq[pivot_index]
    elif len(theSeq)-pivot_index > K:
        return _nth_element(theSeq, pivot_index+1, last, K)
    else:
        return _nth_element(theSeq, first, pivot_index-1, K)

"""
Linear-Time Sorting
"""

def counting_sort(theSeq, k):
    """计数排序, O(n+k)
    theSeq中每一个都是介于0到k之间的整数
    """
    length = len(theSeq)
    newList = [0 for _ in range(length)]    # 设置输出序列并初始化
    countList = [0 for _ in range(k+1)]     #设置计数序列并初始化
    for i in theSeq:    # 计算元素theSeq[i]的个数
        countList[i] += 1
    for j in range(1, k+1): # 计算小于theSeq[j]的个数
        countList[j] = countList[j] + countList[j-1]
    for ele in reversed(theSeq):    # 倒序扫描从而保证稳定算法
        newList[countList[ele] - 1] = ele
        countList[ele] -= 1
    return newList

def bucket_sort(theSeq):
    """桶排序, O(n)
    把数组theSeq划分为n个大小相同子区间（桶），每个子区间各自排序，最后合并，计数排序是桶排序的一种特殊情况，可以把计数排序当成每个桶里只有一个元素的情况
    """
    buckets = [0] * ((max(theSeq) - min(theSeq)) + 1)   # 初始化桶元素
    for i in range(len(theSeq)):
        buckets[theSeq[i] - min(theSeq)] += 1
    newList = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            newList += [i + min(theSeq)] * buckets[i]
    return newList

def radix_sort(theSeq, k=3):
    """基数排序
    基数排序一般用于长度相同的元素组成的数组，首先按照最低有效数字进行排序，然后由低位向高位进行
    k=3，默认三位数，如果是四位数，则k=4，以此类推
    """
    newList = theSeq
    for i in range(k):
        buckets = [[] for _ in range(10)] # 每一位数字都是0~9
        for num in newList:
            buckets[(num / (10 ** i)) % 10].append(num)
        newList = [ele for bucket in buckets for ele in bucket]
    return newList

# test
def test_sort():
    seq0 = [2, 4, 1, 3, 8, 5, 7, 6]
    seq1 = [5, 1, 7, 3, 9, 13, 11]
    seq2 = [8, 4, 10, 2, 6, 12, 0]
    bubble_sort(seq0)
    select_sort(seq1)
    insertion_sort(seq2)

    assert seq0 == list(range(1, 9))
    assert seq1 == list(range(1, 14, 2))
    assert seq2 == list(range(0, 13, 2))
    assert merge_sorted_list(seq1, seq2) == list(range(14))

    seq0 = [2, 4, 1, 3, 8, 5, 7, 6]
    seq1 = [5, 1, 7, 3, 9, 13, 11]
    seq2 = [8, 4, 10, 2, 6, 12, 0]

    assert mergesort(seq0) == list(range(1, 9))
    assert partitionSeq(seq1, 0, len(seq1)-1) == 5
    assert partitionSeq(seq2, 0, len(seq2)-1) == 0
    quicksort(seq1)
    assert seq1 == list(range(1, 14, 2))
    assert nth_element(seq2, 3) == 8

if __name__ == '__main__':
    test_sort()
