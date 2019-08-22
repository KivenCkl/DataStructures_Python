from queue import Queue


class _ExpTreeNode:

    __slots__ = ('element', 'left', 'right')

    def __init__(self, data):
        self.element = data
        self.left = None
        self.right = None

    def __repr__(self):
        return '<_ExpTreeNode: {} {} {}>'.format(self.element, self.left,
                                                 self.right)


class ExpressionTree:
    """ 表达式数

    操作符存储在内节点操作数存储在叶子节点的二叉树
            *
           / \
          +   -
         / \ / \
        9  3 8  4
        (9 + 3) * (8 - 4)

    Expression Tree Abstract Data Type, 可以实现二元操作符

    ExpressionTree(exp_str): user string as constructor param
    evaluate(var_dict): evaluates the expression and returns the numeric result
    toString(): constructs and returns a string represention of the expression

    Usage:
        vars = {'a': 5, 'b': 12}
        exp_tree = ExpressionTree("a/(b-3)")
        print('The result =', exp_tree.evaluate(vars))
    """

    def __init__(self, exp_str):
        self._exp_tree = None
        self._buildTree(exp_str)

    def evaluate(self, var_dict):
        return self._evalTree(self._exp_tree, var_dict)

    def __str__(self):
        return self._buildString(self._exp_tree)

    def _buildString(self, tree_node):
        """ 在一个子树被遍历之前添加左括号，在子树被遍历之后添加右括号
        """
        if tree_node.left is None and tree_node.right is None:
            # 叶子节点是操作数直接返回
            return str(tree_node.element)
        else:
            exp_str = '('
            exp_str += self._buildString(tree_node.left)
            exp_str += str(tree_node.element)
            exp_str += self._buildString(tree_node.right)
            exp_str += ')'
            return exp_str

    def _evalTree(self, subtree, var_dict):
        # 判断是否叶子节点，是的话说明是操作数，直接返回
        if subtree.left is None and subtree.right is None:
            # 判断操作数是否是合法数字
            if '0' <= subtree.element <= '9':
                return int(subtree.element)
            else:
                assert subtree.element in var_dict, 'Invalid variable.'
                return var_dict[subtree.element]
        else:  # 是操作符则计算其子表达式
            lvalue = self._evalTree(subtree.left, var_dict)
            rvalue = self._evalTree(subtree.right, var_dict)
            print(subtree.element)
            return self._computeOp(lvalue, subtree.element, rvalue)

    def _computeOp(self, left, op, right):
        op_func = {
            '+': lambda left, right: left + right,
            '-': lambda left, right: left - right,
            '*': lambda left, right: left * right,
            '/': lambda left, right: left / right,
            '%': lambda left, right: left % right,
        }
        assert op in op_func, 'Invalid operator.'
        return op_func[op](left, right)

    def _buildTree(self, exp_str):
        expQ = Queue()
        for token in exp_str:
            expQ.put(token)
        self._exp_tree = _ExpTreeNode(None)
        self._recBuildTree(self._exp_tree, expQ)

    def _recBuildTree(self, cur_node, expQ):
        token = expQ.get()
        if token == '(':
            cur_node.left = _ExpTreeNode(None)
            self._recBuildTree(cur_node.left, expQ)
            # next token will be an operator: +-*/%
            cur_node.element = expQ.get()
            cur_node.right = _ExpTreeNode(None)
            self._recBuildTree(cur_node.right, expQ)
            # the next token will be ')', remove it
            expQ.get()
        else:  # the token is a digit that has to be converted to an int
            cur_node.element = token


if __name__ == '__main__':
    vars = {'a': 5, 'b': 12}
    exp_tree = ExpressionTree("((a*7)+b)")
    print(exp_tree)
    print('The result =', exp_tree.evaluate(vars))
