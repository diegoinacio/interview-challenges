class Node(object):
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = Node(value)

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = Node(value)

    def __str__(self):
        return str(self._data)


class BinaryTree(object):
    def __init__(self, value=None):
        self._root = Node(value) if value else value

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = Node(value)


def get_preOrder(root: Node, order=[]) -> list:
    if root:
        # First get the data of node
        order += [root.data]
        # Then recur on left child 
        get_preOrder(root.left, order)
        # Finally recur on right child 
        get_preOrder(root.right, order)
    # Return a list of order
    return order

def get_postOrder(root: Node, order=[]) -> list:
    if root:
        # First recur on left child 
        get_postOrder(root.left, order)
        # Then recur on right child 
        get_postOrder(root.right, order)
        # Finally get the data of node
        order += [root.data]
    # Return a list of order
    return order

def get_inOrder(root: Node, order=[]) -> list:
    if root:
        # First recur on left child 
        get_inOrder(root.left, order)
        # Then get the data of node
        order += [root.data]
        # Finally recur on right child 
        get_inOrder(root.right, order)
    # Return a list of order
    return order

def get_height(root: Node) -> int:
    return max(
        get_height(root.left),
        get_height(root.right)
    ) + 1 if root else - 1
