import sys
sys.path.append('../')

from Array_List.array_and_list import Array


class HashMap:
    """
    HashMap ADT 实现，类似于 python 内置的 dict
    一个槽有三种状态：
    1. 从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2. 使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素仍可能是有 key 的
    3. 槽正在使用_MapEntry 节点
    """

    class _MapEntry:  # 槽里存储的数据
        def __init__(self, key, value):
            self.key = key
            self.value = value

    UNUSED = None  # 没被使用过的槽
    EMPTY = _MapEntry(None, None)  # 使用过但是被删除的槽

    def __init__(self):
        self._table = Array(7)  # 初始化 7 个槽
        self._count = 0
        # 超过 2/3 空间被使用就重新分配，load_factor = 2/3
        self._maxCount = len(self._table) - len(self._table) // 3

    def __len__(self):
        return self._count

    def __contains__(self, key):
        slot = self._findSlot(key, False)
        return slot is not None

    def add(self, key, value):
        if key in self:  # 覆盖原有 value
            slot = self._findSlot(key, False)
            self._table[slot].value = value
            return False
        else:
            slot = self._findSlot(key, True)
            self._table[slot] = HashMap._MapEntry(key, value)
            self._count += 1
            if self._count == self._maxCount:  # 超过 2/3 使用就 rehash
                self._rehash()
            return True

    def valueOf(self, key):
        slot = self._findSlot(key, False)
        assert slot is not None, 'Invalid map key'
        return self._table[slot].value

    def remove(self, key):
        """remove 操作把槽置为 EMPTY
        """
        assert key in self, 'Key error {0}'.format(key)
        slot = self._findSlot(key, forInsert=False)
        value = self._table[slot].value
        self._count -= 1
        self._table[slot] = HashMap.EMPTY
        return value

    def __iter__(self):
        return _HashMapIterator(self._table)

    def _slot_can_insert(self, slot):
        return (self._table[slot] is HashMap.EMPTY
                or self._table[slot] is HashMap.UNUSED)

    def _findSlot(self, key, forInsert=False):
        """
        :param forInsert: bool, if the search is for an insertion
        :return: slot or None
        """
        slot = self._hash1(key)
        step = self._hash2(key)
        _len = len(self._table)

        if not forInsert:  # 查找是否存在 key
            while self._table[slot] is not HashMap.UNUSED:
                # 如果一个槽是 UNUSED，直接跳出
                if self._table[slot] is HashMap.EMPTY:
                    slot = (slot + step) % _len
                    continue
                elif self._table[slot].key == key:
                    return slot
                slot = (slot + step) % _len
            return None
        else:  # 为了插入 key
            while not self._slot_can_insert(slot):
                # 循环直到找到一个可以插入的槽
                slot = (slot + step) % _len
            return slot

    def _rehash(self):
        """
        当前使用槽数量大于 2/3 时，重新创建新的 table
        """
        originTable = self._table
        newSize = len(self._table) * 2 + 1  # 原来的 2*n+1 倍
        self._table = Array(newSize)

        self._count = 0
        self._maxCount = newSize - newSize // 3

        # 将原来的 key, value 添加到新的 table
        for entry in originTable:
            if entry is not HashMap.UNUSED and entry is not HashMap.EMPTY:
                slot = self._findSlot(entry.key, True)
                self._table[slot] = entry
                self._count += 1

    def _hash1(self, key):
        """
        计算 key 的 hash 值
        """
        return abs(hash(key)) % len(self._table)

    def _hash2(self, key):
        """
        key 冲突时用来计算新槽的位置
        """
        return 1 + abs(hash(key)) % (len(self._table) - 2)


class _HashMapIterator:
    def __init__(self, array):
        self._array = array
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx <len(self._array):
            if (self._array[self._idx] is not None
                    and self._array[self._idx].key is not None):
                key = self._array[self._idx].key
                self._idx += 1
                return key
            else:
                self._idx += 1
        else:
            raise StopIteration


def print_h(h):
    for idx, i in enumerate(h):
        print(idx, i)
    print('\n')


def test_HashMap():
    h = HashMap()
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

    n = 10
    for i in range(n):
        h.add(str(i), i)
    assert len(h) == n
    print_h(h)
    for i in range(n):
        assert str(i) in h
    for i in range(n):
        h.remove(str(i))
    assert len(h) == 0


if __name__ == '__main__':
    test_HashMap()
