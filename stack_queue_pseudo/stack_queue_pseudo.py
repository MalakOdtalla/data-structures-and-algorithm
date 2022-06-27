from stack_and_queue.stack_and_queue.Stack import Stack

class PseudoQueue:
    def __init__(self):
        self.firststack = Stack()
        self.secondstack = Stack()



    def enqueue(self, value):
        self.firststack.push(value)

    def dequeue(self):
        if (self.firststack.top == None and self.secondstack.top == None):
            return "Queue is empty"
        if (self.secondstack.top == None):
            while self.firststack.top:
                self.secondstack.push(self.firststack.pop())
        removed = self.secondstack.pop()

        return removed


if __name__ == "__main__":
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)


    # print(queue.firststack.top.value)
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())


