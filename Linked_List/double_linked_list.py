class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircularDoubleLinkedList:
    """
    循环双端链表
    """

    def __init__(self, maxsize=None):
        """
        :param maxsize: int or None
        """
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        tailnode = self.tailnode() or self.root
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        if self.root.next is self.root:  # 链表为空
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, value):
        if len(self) == 0:
            raise Exception('Can not remove a node from an empty LinkedList')
        curNode = self.headnode()
        while curNode is not self.root:
            if curNode.value == value:
                self.length -= 1
                return value
            curNode = curNode.next
        return -1

    def append_node(self, node):
        tailnode = self.tailnode()
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def remove_node(self, node):
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        """
        较方便的实现反序遍历
        """
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode


def test_double_link_list():
    dll = CircularDoubleLinkedList()
    assert len(dll) == 0

    dll.append(0)
    dll.append(1)
    dll.append(2)
    assert list(dll) == [0, 1, 2]

    assert [node.value for node in dll.iter_node()] == [0, 1, 2]
    assert [node.value for node in dll.iter_node_reverse()] == [2, 1, 0]

    headnode = dll.headnode()
    assert headnode.value == 0
    dll.remove_node(headnode)
    assert len(dll) == 2
    assert [node.value for node in dll.iter_node()] == [1, 2]

    dll.appendleft(0)
    assert [node.value for node in dll.iter_node()] == [0, 1, 2]

    tailnode = dll.tailnode()
    assert tailnode.value == 2
    assert dll.remove(2) == 2
    dll.append_node(tailnode)
    assert [node.value for node in dll.iter_node()] == [0, 1, 2]


if __name__ == '__main__':
    test_double_link_list()
