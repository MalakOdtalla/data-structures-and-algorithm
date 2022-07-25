from trees.tree_fizz_buzz.tree_fizz_buzz import fizz_buzz_tree,Node,kTree

def test_fizz_buz():
    tree = kTree()
    tree.root = Node(2)
    tree.root.left = Node(10)
    tree.root.right = Node(15)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(3)
    tree.root.right.right = Node(9)
    tree.root.right.left = Node(4)

    new = fizz_buzz_tree(tree)
    assert new == ['2', 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz', '4', 'Fizz']


