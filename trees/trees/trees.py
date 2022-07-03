class Node:
    def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """returns array of values ordered root, left, right"""
        output = []
        def _walk(root):
            if not root:
                return 'empty tree'

            output.append(root.value)
            _walk(root.left)
            _walk(root.right)

        _walk(self.root)
        return output

    def in_order(self):
        """returns array of values ordered left, root, right"""
        output = []
        def walk(root):
            """navigates tree"""
            if not root:
                return
            walk(root.left) # check left
            output.append(root.value) # root
            walk(root.right) # check right
        walk(self.root)
        return output

    def post_order(self):
        """returns array of values ordered left, right, root"""
        output = []
        def walk(root):
            """navigates tree"""
            if not root:
                return
            walk(root.left)
            walk(root.right)
            output.append(root.value)
        walk(self.root)
        return output


class BinarySearchTree(BinaryTree):
    def add(self, value):

        '''
        add value to binery tree
        '''
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while (current):
                if current.value > value:
                    if current.left == None:
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None:
                        current.right = Node(value)
                        break
                    current = current.right

    def contains(self, value):
         """check the value is in the tree at least once."""

         if self.root == None:
             raise "its empty tree "


         else:
             def _walk(root):
                 if root:
                     if value == root.value:
                         return True
                     elif value < root.value:
                         return _walk(root.left)
                     elif value > root.value:
                         return _walk(root.right)
                 return False

             return _walk(self.root)

if __name__ == "__main__":
     tree=BinaryTree()
     tree.root = Node(1)
     tree.root.right = Node(2)
     tree.root.left = Node(3)
     tree.root.right.left = Node(4)
     tree.root.left.left = Node(5)
     tree.root.right.right = Node(6)
     print(tree.pre_order())
     print(tree.in_order())
     print(tree.post_order())


     Tree=BinarySearchTree()
     Tree.add(9)

     print(Tree.contains(9))