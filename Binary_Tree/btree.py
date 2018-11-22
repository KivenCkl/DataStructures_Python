from queue import Queue

class _BinTreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
class BinTree:
    
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def built_from(cls, node_list):
        """build_from

        :param node_list: 
            {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = _BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)

    # 三种depth-first遍历
    def preOrderTrav(self, subtree):
        """先（根）序遍历

        前序遍历是指，对于树中的任意节点来说，先打印这个节点，然后再打印它的左子树，最后打印它的右子树
        """
        if subtree is not None:
            print(subtree.data)
            self.preOrderTrav(subtree.left)
            self.preOrderTrav(subtree.right)

    def inOrderTrav(self, subtree):
        """中（根）序遍历

        中序遍历是指，对于树中的任意节点来说，先打印它的左子树，然后再打印它本身，最后打印它的右子树
        """
        if subtree is not None:
            self.inOrderTrav(subtree.left)
            print(subtree.data)
            self.inOrderTrav(subtree.right)

    def postOrderTrav(self, subtree):
        """后（根）序遍历
        
        后序遍历是指，对于树中的任意节点来说，先打印它的左子树，然后再打印它的右子树，最后打印这个节点本身
        """
        if subtree is not None:
            self.postOrderTrav(subtree.left)
            self.postOrderTrav(subtree.right)
            print(subtree.data)

    # 宽度优先遍历(breadth-First Traversal): 一层一层遍历，使用queue
    def breadthFirstTrav(self, bintree):
        q = Queue()
        q.put(bintree)
        while not q.empty():
            node = q.get()
            print(node.data)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)


def test_binTree():
    """
        A
       / \\
      B   C
     / \ / \\
    D  E F  G
      /    / \\
     H    I   J
    """
    node_list = [
        {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
        {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
        {'data': 'D', 'left': None, 'right': None, 'is_root': False},
        {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
        {'data': 'H', 'left': None, 'right': None, 'is_root': False},
        {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
        {'data': 'F', 'left': None, 'right': None, 'is_root': False},
        {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
        {'data': 'I', 'left': None, 'right': None, 'is_root': False},
        {'data': 'J', 'left': None, 'right': None, 'is_root': False},
    ]
    btree = BinTree.built_from(node_list)
    print('----')
    btree.preOrderTrav(btree.root)
    print('----')
    btree.inOrderTrav(btree.root)
    print('----')
    btree.postOrderTrav(btree.root)
    print('----')
    btree.breadthFirstTrav(btree.root)

if __name__ == '__main__':
    test_binTree()
