class Stack_1:
    """
    Stack ADT, using a python list
    """

    def __init__(self):
        self._items = list()

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)

    def peek(self):
        assert not self.isEmpty()
        return self._items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self._items.pop()

    def push(self, item):
        self._items.append(item)


class Stack_2:
    """
    Stack ADT, using linked list
    """

    def __init__(self):
        self._top = None
        self._size = 0

    def isEmpty(self):
        return self._top is None

    def peek(self):
        assert not self.isEmpty()
        return self._top.item

    def pop(self):
        assert not self.isEmpty()
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1


class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link


def test_stack():
    s1 = Stack_1()
    s1.push(0)
    s1.push(1)
    s1.push(2)

    assert s1.pop() == 2
    assert s1.pop() == 1
    assert s1.pop() == 0

    s2 = Stack_2()
    s2.push(2)
    s2.push(4)
    s2.push(6)

    assert s2.isEmpty() == False
    assert s2.pop() == 6
    assert s2.pop() == 4
    assert s2.pop() == 2
    assert s2.isEmpty() == True


if __name__ == '__main__':
    test_stack()