from stack_and_queue.stack_and_queue.Node import Node

class Stack:
    def __init__(self):
        self.top = None


    def push(self, value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):

        try:
            item = self.top
            self.top = self.top.next
            return item.value
        except AttributeError :
            return 'Stack is empty'

    def peek(self):
        try:

            return self.top.value
        except AttributeError :
            return 'Stack is empty'

    def is_empty(self):
        if self.top:
            return False
        else :
            return True



if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print (stack.top.value)

    print(stack.pop())
    # print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
