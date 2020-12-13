# TODO: Implement TreeNode class
class TreeNode:
    def __init__(self, value):
        self._value = value
        self._right = None
        self._left = None

    @property
    def value(self):
        return self._value

    @property
    def right(self):
        return self._right

    @property
    def left(self):
        return self._left

    @value.setter
    def value(self, value):
        self._value = value

    @right.setter
    def right(self, node):
        self._right = node

    @left.setter
    def left(self, node):
        self._left = node


node_a = TreeNode('a')
print(node_a.value)         # 'a'
node_a.right = TreeNode('c')
print(node_a.right)         # <__main__.TreeNode object ...
print(node_a.right.value)   # 'c'
print(node_a.left)          # None


node_b = TreeNode('b')
node_a.left = node_b
print(node_a.left.value)    # 'b'
print(node_a.right)         # None
