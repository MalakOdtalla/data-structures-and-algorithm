from trees.trees.trees import BinaryTree,Node
from trees.trees.tree_breadth_first.tree_breadth_first import BinaryTree
from trees.trees.tree_fizz_buzz.tree_fizz_buzz import fizz_buzz_tree

def test_fizz_buz():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(10)
    tree.root.right = Node(15)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(3)
    tree.root.right.right = Node(9)
    tree.root.right.left = Node(4)

    new = fizz_buzz_tree(tree)
    assert tree.breadth_first(new.root) == ['2', 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz', '4', 'Fizz']


