from stack_and_queue.stack_and_queue.Node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear= None

    def enqueue(self, value):
        node = Node(value)

        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        try:
            item = self.front
            self.front = self.front.next
            return item.value
        except AttributeError :
            return 'Queue is empty'


    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return 'Queue is empty'

    def is_empty(self):
        if self.front:
            return False
        else :
            return True

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.rear.value)
    print(queue.dequeue())
    print(queue.peek())
