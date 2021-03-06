import sys
sys.path.append('../')
from Array_List.array_and_list import Array


class _BSTMapNode:
    __slots__ = ('key', 'value', 'left', 'right')

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return '<{}:{}> left:{}, right:{}'.format(self.key, self.value,
                                                  self.left, self.right)

    __str__ = __repr__


class BSTMap:
    """
    BST, 树节点包含 key 可 payload. 用 BST 来实现之前用 hash 实现过的 Map ADT.
    性质：对每个内部节点 V,
    1. 对于节点 V, 所有 key 小于 V.key 的存储在 V 的左子树。
    2. 所有 key 大于 V.key 的存储在 V 的右子树
    对 BST 进行中序遍历会得到升序的 key 序列
    """

    def __init__(self):
        self._root = None
        self._size = 0
        self._rval = None  # 作为 remove 的返回值

    def __len__(self):
        return self._size

    def __iter__(self):
        return _BSTMapIterator(self._root, self._size)

    def __contains__(self, key):
        return self._bstSearch(self._root, key) is not None

    def valueOf(self, key):
        node = self._bstSearch(self._root, key)
        assert node is not None, 'Invalid map key.'
        return node.value

    def _bstSearch(self, subtree, target):
        if subtree is None:  # 递归出口，遍历到树底
            return None
        elif target < subtree.key:
            return self._bstSearch(subtree.left, target)
        elif target > subtree.key:
            return self._bstSearch(subtree.right, target)
        return subtree  # 返回引用

    def _bstMin(self, subtree):
        """
        顺着树一直往左下角递归找就是最小的，向右下角递归就是最大的
        """
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return subtree._bstMin(self, subtree.left)

    def add(self, key, value):
        """
        添加或者替代一个 key 的 value, O(N)
        """
        node = self._bstSearch(self._root, key)
        if node is not None:  # if key already exists, update value
            node.value = value
            return False
        else:  # insert a new entry
            self._root = self._bstInsert(self._root, key, value)
            self._size += 1
            return True

    def _bstInsert(self, subtree, key, value):
        """
        新的节点总是插入在树的叶子节点上
        """
        if subtree is None:
            subtree = _BSTMapNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bstInsert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bstInsert(subtree.right, key, value)
        return subtree

    def remove(self, key):
        """
        O(N)
        被删除的节点分为三种：
        1. 叶子节点：直接把其父亲指向该节点的指针置 None
        2. 该节点有一个 child：删除该节点后，父亲指向一个合适的该节点的孩子
        3. 该节点有两个 child：
            (1) 找到要删除节点 N 和其后继 S (中序遍历后该节点下一个)
            (2) 复制 S 的 ke y 和 N
            (3) 从 N 的右子树中删除后继 S (即在 N 的右子树中最小的)
        """
        assert key in self, 'invalid map key'
        self._root = self._bstRemove(self._root, key)
        self._size -= 1
        return self._rval

    def _bstRemove(self, subtree, target):
        if subtree is None:
            return subtree
        elif target < subtree.key:
            subtree.left = self._bstRemove(subtree.left, target)
            return subtree
        elif target > subtree.key:
            subtree.right = self._bstRemove(subtree.right, target)
            return subtree
        else:
            self._rval = subtree.value
            if subtree.left is None and subtree.right is None:  # 叶子节点
                return None
            elif subtree.left is None or subtree.right is None:  # one child
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:  # two child
                successor = self._bstMin(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self._bstRemove(subtree.right, successor.key)
                return subtree

    def __repr__(self):
        return '->'.join([str(i) for i in self])

    def assert_keep_bst_property(self, subtree):
        """
        写这个函数为了验证 add 和 delete 操作始终维持了 bst 的性质
        """
        if subtree is None:
            return
        if subtree.left is not None and subtree.right is not None:
            assert subtree.left.value <= subtree.value
            assert subtree.right.value >= subtree.value
            self.assert_keep_bst_property(subtree.left)
            self.assert_keep_bst_property(subtree.right)

        elif subtree.left is None and subtree.right is not None:
            assert subtree.right.value >= subtree.value
            self.assert_keep_bst_property(subtree.right)

        elif subtree.left is not None and subtree.right is None:
            assert subtree.left.value <= subtree.value
            self.assert_keep_bst_property(subtree.left)


class _BSTMapIterator:
    def __init__(self, root, size):
        self._theKeys = Array(size)
        self._curItem = 0
        self._bstTraversal(root)
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._theKeys):
            key = self._theKeys[self._curItem]
            self._curItem += 1
            return key
        else:
            raise StopIteration

    def _bstTraversal(self, subtree):
        if subtree is not None:
            self._bstTraversal(subtree.left)
            self._theKeys[self._curItem] = subtree.key
            self._curItem += 1
            self._bstTraversal(subtree.right)


def test_BSTMap():
    l = [60, 25, 100, 35, 17, 80]
    bst = BSTMap()
    for i in l:
        bst.add(i)


def test_HashMap():
    """
    之前用来测试用 hash 实现的 map，改为用 BST 实现的 Map 测试
    """
    # h = HashMap()
    h = BSTMap()
    assert len(h) == 0
    h.add('a', 'a')
    assert h.valueOf('a') == 'a'
    assert len(h) == 1

    a_v = h.remove('a')
    assert a_v == 'a'
    assert len(h) == 0

    h.add('a', 'a')
    h.add('b', 'b')
    assert len(h) == 2
    assert h.valueOf('b') == 'b'
    b_v = h.remove('b')
    assert b_v == 'b'
    assert len(h) == 1
    h.remove('a')

    assert len(h) == 0

    _len = 10
    for i in range(_len):
        h.add(str(i), i)
    assert len(h) == _len
    for i in range(_len):
        assert str(i) in h
    for i in range(_len):
        print(len(h))
        print('bef', h)
        _ = h.remove(str(i))
        assert _ == i
        print('aft', h)
        print(len(h))
    assert len(h) == 0


if __name__ == '__main__':
    test_HashMap()
