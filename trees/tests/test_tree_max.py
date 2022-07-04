from trees.trees.tree_max.tree_max import BinaryTree,Node
import pytest


@pytest.fixture
def check():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.right = Node(2)
    tree.root.left = Node(3)
    tree.root.right.left = Node(4)
    tree.root.left.left = Node(5)
    tree.root.right.right = Node(6)
    return tree

def test_max_value(check):
    actual = check.max_tree()
    expected = 6
    assert actual == expected

def test_max_value_empty_tree():
    tree = BinaryTree()
    actual = tree.max_tree()
    expected = "Tree is Empty"
    assert actual == expected