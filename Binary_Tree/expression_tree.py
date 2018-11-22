from queue import Queue

class _ExpTreeNode:

    __slots__ = ('element', 'left', 'right')

    def __init__(self, data):
        self.element = data
        self.left = None
        self.right = None

    def __repr__(self):
        return '<_ExpTreeNode: {} {} {}>'.format(
            self.element, self.left, self.right
        )


class ExpressionTree:
    """表达式数

    操作符存储在内节点操作数存储在叶子节点的二叉树         
            *
           / \\
          +   -
         / \ / \\
        9  3 8  4
        (9 + 3) * (8 - 4)

    Expression Tree Abstract Data Type, 可以实现二元操作符   
    ExpressionTree(expStr): user string as constructor param    
    evaluate(varDict): evaluates the expression and returns the numeric result
    toString(): constructs and returns a string represention of the expression

    Usage:
        vars = {'a': 5, 'b': 12}
        expTree = ExpressionTree("a/(b-3)")
        print('The result = ', expTree.evaluate(vars))
    """

    def __init__(self, expStr):
        self._expTree = None
        self._buildTree(expStr)

    def evaluate(self, varDict):
        return self._evalTree(self._expTree, varDict)

    def __str__(self):
        return self._buildString(self._expTree)

    def _buildString(self, treeNode):
        """在一个子树被遍历之前添加左括号，在子树被遍历之后添加右括号
        """
        if treeNode.left is None and treeNode.right is None:
            # 叶子节点是操作数直接返回
            return str(treeNode.element)
        else:
            expStr = '('
            expStr += self._buildString(treeNode.left)
            expStr += str(treeNode.element)
            expStr += self._buildString(treeNode.right)
            expStr += ')'
            return expStr

    def _evalTree(self, subtree, varDict):
        # 判断是否叶子节点，是的话说明是操作数，直接返回
        if subtree.left is None and subtree.right is None:
            # 判断操作数是否是合法数字
            if '0' <= subtree.element <= '9':
                return int(subtree.element)
            else:
                assert subtree.element in varDict, 'Invalid variable.'
                return varDict[subtree.element]
        else:   # 是操作符则计算其子表达式
            lvalue = self._evalTree(subtree.left, varDict)
            rvalue = self._evalTree(subtree.right, varDict)
            print(subtree.element)
            return self._computeOp(lvalue, subtree.element, rvalue)

    def _computeOp(self, left, op, right):
        assert op
        op_func = {
            '+': lambda left, right: left + right,  
            '-': lambda left, right: left - right,  
            '*': lambda left, right: left * right, 
            '/': lambda left, right: left / right, 
            '%': lambda left, right: left % right,
        }
        return op_func[op](left, right)

    def _buildTree(self, expStr):
        expQ = Queue()
        for token in expStr:
            expQ.put(token)
        self._expTree = _ExpTreeNode(None)
        self._recBuildTree(self._expTree, expQ)

    def _recBuildTree(self, curNode, expQ):
        token = expQ.get()
        if token == '(':
            curNode.left = _ExpTreeNode(None)
            self._recBuildTree(curNode.left, expQ)
            # next token will be an operator: +-*/%
            curNode.element = expQ.get()
            curNode.right = _ExpTreeNode(None)
            self._recBuildTree(curNode.right, expQ)
            # the next token will be ')', remove it
            expQ.get()
        else:   # the token is a digit that has to be converted to an int
            curNode.element = token

def test_exp_tree():
    vars = {'a': 5, 'b': 12}
    expTree = ExpressionTree("((a*7)+b)")
    print(expTree)
    print('The result = ', expTree.evaluate(vars))

if __name__ == '__main__':
    test_exp_tree()