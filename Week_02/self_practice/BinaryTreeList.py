"""BinaryTree using list"""
from doctest import testmod


def binary_tree(root: int):
    """
    This function returns a binary tree, use root as root
    :param root: The value of root node
    :return: Binary tree in list format

    >>> binary_tree(3)
    [3, [], []]
    >>> binary_tree(4)
    [4, [], []]
    """
    return [root, [], []]


def insert_left(root: list, new_branch: int):
    """
    For a given node, insert new branch to the left
    :param root: The root node
    :param new_branch: Value of new branch
    :return: None

    >>> insert_left([3, [], []], 4)
    [3, [4, [], []], []]
    """
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    print(root)


def insert_right(root: list, new_branch: int):
    """
    For a given node, insert new branch to the right

    :param root: The root node
    :param new_branch: Value of new branch
    :return: None

    >>> root = [3, [], []]
    >>> insert_right(root, 4)
    >>> print(root)
    [3, [], [4, [], []]]
    """
    t = root.pop(2)
    if len(t) > 0:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])


def get_root_val(root: list):
    """
    Return the value of root
    :param root node
    return

    >>> get_root_val([3, [], []])
    3
    """
    return root[0]


def set_root_val(root, new_value):
    """
    Set root value
    :param root: root node
    :param new_value: The new value in int
    :return: None

    >>> set_root_val([3, [], []], 4)
    4
    """
    root[0] = new_value if new_value is not isinstance(new_value, int) else 0
    return root[0]


def get_left_child(root):
    """
    Return given root left node
    :param root: root node
    :return: Left node in list format

    >>> get_left_child([3, [2, [], []], []])
    [2, [], []]
    """
    return root[1]


def get_right_child(root):
    """
    Return given root left node
    :param root: root node
    :return: Left node in list format

    >>> get_right_child([3, [2, [], []], [4, [], []]])
    [4, [], []]
    """
    return root[2]


if __name__ == '__main__':
    testmod(verbose=True)
    b_tree = binary_tree(3)
    print(b_tree)
    insert_left(b_tree, 4)
    print(b_tree)
    insert_left(b_tree, 5)
    print(b_tree)
    set_root_val(b_tree, 'aa')
    print(b_tree)

