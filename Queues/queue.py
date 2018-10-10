# 顺序队列
class Queue_List:
    """Queue ADT, use list
    """

    def __init__(self):
        self._qList = list()
    
    def isEmpty(self):
        return len(self) == 9
    
    def __len__(self):
        return len(self._qList)
    
    def enqueue(self, item):
        self._qList.append(item)
    
    def dequeue(self):
        assert not self.isEmpty()
        return self._qList.pop(0)

# 循环队列
import sys
sys.path.append('C:/Users/chenkiven/Desktop/Code/data_structures_python')
from Array_List.array_and_list import Array
class Queue_Cir_Array:
    """Queue ADT, use Circular Array
        通过头尾指针实现，使用环数组实现可以使得入队出队操作时间复杂度为O(1)，缺点是数组长度需要固定
    """
    def __init__(self, maxSize):
        self._count = 0
        self._head = 0
        self._tail = maxSize - 1
        self._qArray = Array(maxSize)

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return self._count == len(self._qArray)

    def __len__(self):
        return len(self._count)

    def enqueue(self, item):
        assert not self.isFull()
        maxSize = len(self._qArray)
        self._tail = (self._tail + 1) % maxSize     # 移动尾指针
        self._qArray[self._tail] = item
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty()
        item = self._qArray[self._head]
        maxSize = len(self._qArray)
        self._head = (self._head + 1) % maxSize
        self._count -= 1
        return item

# 链式队列
class Queue_Linked_List:
    """Queue ADT, use linked list
        改进环数组有最大数量的限制，改用带有头尾节点的linked list实现
    """
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._qsize = 0
    
    def isEmpty(self):
        return self._qhead is None

    def __len__(self):
        return self._qsize

    def enqueue(self, item):
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node
        self._qtail = node
        self._qsize += 1

    def dequeue(self):
        assert not self.isEmpty(), 'Can not dequeue form an empty queue'
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._qsize -= 1
        return node.item

class _QueueNode:
    def __init__(self, item):
        self.item = item
        self.next = None

"""
PriorityQueue ADT: 给每个item加上优先级p，高优先级先dequeue
分为两种：
- bounded PriorityQueue: 限制优先级在一个区间[0...p)
- unbounded PriorityQueue: 不限制优先级

两种实现方式：
1. 入队的时候都是到队尾，出队操作找到最高优先级的出队，出队操作O(n)
2. 始终维持队列有序，每次入队都找到该插入的位置，出队操作是O(1)
"""
class UnboundedPriorityQueue:
    """
    """
    from collections import namedtuple
    _PriorityQEntry = namedtuple('_PriorityQEntry', 'item, priority')

    # 采用方式1
    def __init__(self):
        self._qlist = list()

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._qlist)

    def enqueue(self, item, priority):
        entry = UnboundedPriorityQueue._PriorityQEntry(item, priority)
        self._qlist.append(entry)

    def dequeue(self):
        assert not self.isEmpty(), 'can not dequeue from an empty queue'
        highest = self._qlist[0].priority
        temp = 0
        for i in range(1, len(self)):
            if self._qlist[i].priority < highest:
                temp = i
                highest = self._qlist[i].priority
        entry = self._qlist.pop(temp)
        return entry.item

class BoundedPriorityQueue:
    """BoundedPriorityQueue ADT, use linked list
    BoundedPriorityQueue的优先级限制在[0, maxPriority-1]
    对于UnboundedPriorityQueue，出队操作由于要遍历寻找优先级最高的item，所以平均是O(n)的操作；
    但是对于BoundedPriorityQueue，用队列数组实现可以达到常量时间，用空间换时间；
    比如，要弹出一个元素，直接找到第一个非空队列弹出元素即可（小数字代表高优先级，先出队）

    qList
    [0] -> ["white"]
    [1]
    [2] -> ["balck", "green"]
    [3] -> ["purple", "yellow"]
    """
    from Array_List.array_and_list import Array     # 之前定义的数组

    def __init__(self, numLevels):
        self._qSize = 0
        self._qLevels = Array(numLevels)
        for i in range(numLevels):
            self._qLevels[i] = Queue_Linked_List()  # 前面定义的链式队列
    
    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._qSize

    def enqueue(self, item, priority):
        assert priority >= 0 and priority < len(self._qLevels), 'invalid priority'
        self._qSize += 1
        self._qLevels[priority].enqueue(item)
    
    def dequeue(self):
        assert not self.isEmpty(), 'can not dequeue from an empty queue'
        i = 0
        p = len(self._qLevels)
        while i < p and self._qLevels[i].isEmpty(): # 找到第一个非空队列
            i += 1
        self._qSize -= 1
        return self._qLevels[i].dequeue()


def test_queue():
    ql = Queue_List()
    ql.enqueue(1)
    ql.enqueue(2)
    ql.enqueue(3)
    assert ql.dequeue() == 1
    assert ql.dequeue() == 2
    assert ql.dequeue() == 3

    qll = Queue_Linked_List()
    qll = Queue_List()
    qll.enqueue(1)
    qll.enqueue(2)
    qll.enqueue(3)
    assert qll.dequeue() == 1
    assert qll.dequeue() == 2
    assert qll.dequeue() == 3

    qc = Queue_Cir_Array(3)
    qc.enqueue(1)
    qc.enqueue(2)
    qc.enqueue(3)
    assert qc.isFull()
    assert qc.dequeue() == 1
    assert qc.dequeue() == 2
    assert qc.dequeue() == 3
    assert qc.isEmpty()

    ubpq = UnboundedPriorityQueue()
    ubpq.enqueue(1, 2)
    ubpq.enqueue(2, 3)
    ubpq.enqueue(3, 2)
    ubpq.enqueue(4, 1)
    assert ubpq.dequeue() == 4
    assert ubpq.dequeue() == 1
    assert ubpq.dequeue() == 3
    assert ubpq.dequeue() == 2
    assert ubpq.isEmpty()

    bpq = BoundedPriorityQueue(numLevels=3)
    bpq.enqueue(2, 2)
    bpq.enqueue(3, 1)
    bpq.enqueue(5, 1)
    bpq.enqueue(1, 0)
    assert bpq.dequeue() == 1
    assert bpq.dequeue() == 3
    assert bpq.dequeue() == 5
    assert bpq.dequeue() == 2
    assert bpq.isEmpty()


if __name__ == '__main__':
    test_queue()
