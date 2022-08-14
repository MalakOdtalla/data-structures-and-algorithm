from trees.trees.trees import Node,BinaryTree

from tree_intersection import tree_intetsaction

def test_empty_tree():
    tree1=BinaryTree()
    tree2 = BinaryTree()
    assert tree_intetsaction(tree1,tree2) == []

def test_tree_intetsaction():
    tree1=BinaryTree()
    tree2 = BinaryTree()
    tree1.root = Node(150)
    tree1.root.right = Node(250)
    tree1.root.right.left = Node(200)
    tree1.root.right.right= Node(350)
    tree1.root.right.right.right = Node(300)
    tree1.root.right.right.left = Node(500)
    tree1.root.left = Node(100)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(160)
    tree1.root.left.right.left = Node(125)
    tree1.root.left.right.right = Node(175)

    tree2.root = Node(42)
    tree2.root.right = Node(600)
    tree2.root.right.left = Node(200)
    tree2.root.right.right= Node(350)
    tree2.root.right.right.right = Node(4)
    tree2.root.right.right.left = Node(500)
    tree2.root.left = Node(100)
    tree2.root.left.left = Node(15)
    tree2.root.left.right = Node(160)
    tree2.root.left.right.left = Node(125)
    tree2.root.left.right.right = Node(175)

    assert tree_intetsaction(tree1, tree2) == [100, 160, 125, 175, 200, 350, 500]
