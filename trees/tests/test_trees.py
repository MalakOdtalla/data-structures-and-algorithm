
from trees.trees.trees import BinaryTree,BinarySearchTree,Node

import pytest


def test_empty_binary_tree():
    tree = BinaryTree()
    assert tree.root == None

def test_single_root():
    tree = BinaryTree()
    tree.root = Node(1)
    assert tree.root.value == 1

def test_left_right():
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(1)
    tree.add(3)
    right = tree.root.right.value
    expected_right = 3
    left = tree.root.left.value
    expected_left = 1
    assert right == expected_right
    assert left == expected_left


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

def test_pre_order(check):
    actual = check.pre_order()
    expected = [1, 3, 5, 2, 4, 6]
    assert actual == expected

def test_in_order(check):
    actual = check.in_order()
    expected = [5, 3, 1, 4, 2, 6]
    assert actual == expected

def test_post_order(check):
    actual = check.post_order()
    expected = [5, 3, 4, 6, 2, 1]
    assert actual == expected


def test_contains():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    actual = tree.contains(2)
    expected = True
    assert actual ==expected

