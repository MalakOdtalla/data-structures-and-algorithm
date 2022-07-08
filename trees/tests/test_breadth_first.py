from trees.trees.tree_breadth_first.tree_breadth_first import BinaryTree,Node
import pytest


@pytest.fixture
def check():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.right.right = Node(9)

    tree.root.left.right.right = Node(11)
    tree.root.left.right.left = Node(5)
    tree.root.right.right.left = Node(4)


    return tree

def test_breadth_first(check):
    Actual=check.breadth_first(check.root)
    expected=[2,7,5,2,6,9,5,11,4]
    assert Actual== expected