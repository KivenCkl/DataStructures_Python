"""
利用循环双端链表可以实现一个经典的缓存失效算法，LRU
"""
# from double_linked_list import Node, CircularDoubleLinkedList

# class LRU_Node(Node):
#     def __init__(self, prev=None, next=None, key=None, value=None):
#         Node.__init__(self, value, prev, next)
#         self.key = key

# class LRUCache:

#     def __init__(self, maxsize=16):
#         self.maxsize = maxsize
#         self.cache = {}
#         self.access = CircularDoubleLinkedList()
#         self.isfull = len(self.cache) >= self.maxsize

#     def __call__(self, func):
#         def wrapper(n):
#             cachenode = self.cache.get(n)
#             if cachenode is not None:   # hit
#                 self.access.remove_node(cachenode)
#                 self.access.append_node(cachenode)
#                 return cachenode.value
#             else:   # miss
#                 value = func(n)
#                 if not self.isfull:
#                     tailnode = self.access.tailnode()
#                     newnode = LRU_Node(tailnode, self.access.root, n, value)
#                     # newnode = LRU_Node(key=n, value=value)
#                     self.access.append_node(newnode)
#                     self.cache[n] = newnode
#                     self.isfull = len(self.cache) >= self.maxsize
#                     return value
#                 else:   # full
#                     lru_node = self.access.headnode()
#                     del self.cache[lru_node.key]
#                     self.access.remove_node(lru_node)
#                     tailnode = self.access.tailnode()
#                     newnode = LRU_Node(tailnode, self.access.root, n, value)
#                     # newnode = LRU_Node(key=n, value=value)
#                     self.access.append(newnode)
#                     self.cache[n] = newnode
#                 return value
#         return wrapper

from double_linked_list import Node, CircularDoubleLinkedList


class LRU_Node(Node):
    def __init__(self, prev=None, next=None, key=None, value=None):
        Node.__init__(self, value, prev, next)
        self.key = key


class LRUCache:
    def __init__(self, maxsize=16):
        self.maxsize = maxsize
        self.cache = {}
        self.access = CircularDoubleLinkedList()
        self.isfull = len(self.cache) >= maxsize

    def __call__(self, func):
        def wrapper(*arg):
            cachenode = self.cache.get(arg)
            if cachenode is not None:
                self.access.remove_node(cachenode)
                self.access.append_node(cachenode)
                return cachenode.value
            else:
                value = func(*arg)
                if self.isfull:
                    lru_headnode = self.access.headnode()
                    del self.cache[lru_headnode.key]
                    self.access.remove_node(lru_headnode)
                newnode = LRU_Node(key=arg, value=value)
                self.access.append_node(newnode)
                self.cache[arg] = newnode
                self.isfull = len(self.cache) >= self.maxsize
                return value

        return wrapper


def test():
    @LRUCache()
    def fib(n):
        if n <= 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    for i in range(1, 35):
        print(fib(i))


if __name__ == '__main__':
    test()
