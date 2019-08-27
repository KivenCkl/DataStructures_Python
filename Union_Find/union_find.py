"""
Union-Find
并查集
"""


class Quick_Find:
    """Quick-Find 算法
    时间复杂度：
        Constructor: O(N)
        Union: O(N)
        Find: O(1)
    """

    def __init__(self, n):
        """初始化 uf 数组和组数目"""
        self._count = n  # number of components
        # access to component id (site indexed)
        self.uf = [i for i in range(n)]

    def find(self, x):
        """判断节点所属于的组"""
        return self.uf[x]

    def union(self, x, y):
        """连接两个节点"""
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        for i, v in enumerate(self.uf):
            if v == x_root:
                self.uf[i] = y_root
        self._count -= 1

    def connected(self, x, y):
        """判断两个节点是否联通"""
        return self.find(x) == self.find(y)

    @property
    def count(self):
        """返回所有组的数目"""
        return self._count


class Quick_Union:
    """Quick-Union 算法
    时间复杂度：
        Constructor: O(N)
        Union: O(Tree height)
        Find: O(Tree height)
    """

    def __init__(self, n):
        """初始化 uf 数组和组数目"""
        self._count = n  # number of components
        # access to component id (site indexed)
        self.uf = [i for i in range(n)]

    def find(self, x):
        """判断节点所属于的组"""
        while x != self.uf[x]:
            x = self.uf[x]
        return self.uf[x]

    def union(self, x, y):
        """连接两个节点"""
        x_root = self.find(x)
        y_root = self.find(y)
        self.uf[x_root] = y_root
        self._count -= 1

    def connected(self, x, y):
        """判断两个节点是否联通"""
        return self.find(x) == self.find(y)

    @property
    def count(self):
        """返回所有组的数目"""
        return self._count


class Optimized_Quick_Union:
    """Weighted Quick-Union With Path Compression 算法
    时间复杂度：
        Constructor: O(N)
        Union: near O(1)
        Find: near O(1)
    """

    def __init__(self, n):
        """
        初始化 uf 数组和组数目
        """
        self._count = n  # number of components
        # access to component id (site indexed)
        self.uf = [i for i in range(n)]
        # 用于统计某一个集合中元素的个数
        self.counter = {i: 1 for i in range(n)}

    def find(self, x):
        """
        判断节点所属于的组
        """
        while x != self.uf[x]:
            # 将节点的父节点指向该节点爷爷节点，从而对路径进行压缩
            self.uf[x] = self.uf[self.uf[x]]
            x = self.uf[x]
        return self.uf[x]

    def union(self, x, y):
        """
        连接两个节点
        """
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            # 更改对应集合的元素个数
            # 永远将祖先记为集合中元素最小的那个数
            if x_root < y_root:
                self.uf[y_root] = x_root
                self.counter[x_root] += self.counter[y_root]
            else:
                self.uf[x_root] = y_root
                self.counter[y_root] += self.counter[x_root]
        self._count -= 1

    def connected(self, x, y):
        """
        判断两个节点是否联通
        """
        return self.find(x) == self.find(y)

    @property
    def count(self):
        """
        返回所有组的数目
        """
        return self._count


if __name__ == "__main__":
    union_find = Optimized_Quick_Union(10)
    union_find.union(1, 5)
    union_find.union(2, 4)
    union_find.union(5, 6)
    union_find.union(3, 9)
    union_find.union(8, 9)
    print(union_find.count)
    print(union_find.find(5))
    assert union_find.connected(1, 6) == True
    print(union_find.uf)
    print(union_find.counter)
