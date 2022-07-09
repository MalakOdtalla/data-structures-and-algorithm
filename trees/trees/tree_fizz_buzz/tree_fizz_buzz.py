from trees.trees.trees import BinaryTree,Node
from trees.trees.tree_breadth_first.tree_breadth_first import BinaryTree

def fizz_buzz(value):
    """
    Function to do the fizz_buzz on the given value

    """
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    else:
        return str(value)


def fizz_buzz_tree(tree):
        """
        Function to change all values in the given tree according to fizz_buzz

        """

        new_tree = BinaryTree()
        if not tree.root:
            return new_tree

        def _walk(current):
            """
             function to use in recursion to add new values in the new_tree according to their positions in the tree
            """
            node = Node(fizz_buzz(current.value))
            if current.left:
                node.left = _walk(current.left)
            if current.right:
                node.right = _walk(current.right)
            return node
        new_tree.root = _walk(tree.root)

        return new_tree



if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(10)
    tree.root.right = Node(15)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(3)
    tree.root.right.right = Node(9)
    tree.root.right.left = Node(4)



    new = fizz_buzz_tree(tree)
    print(tree.breadth_first(new.root))


