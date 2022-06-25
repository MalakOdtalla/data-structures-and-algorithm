# from stack_and_queue.stack_and_queue.Node import Node
from stack_and_queue.stack_and_queue.Queue import Queue
from stack_and_queue.stack_and_queue.Stack import Stack

# Stack tests

def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.top.value == 3

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop()==3


def test_stack_is_empty():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop()==3
    assert stack.pop() ==2
    assert stack.pop() == 1
    assert stack.is_empty() == True


def test_peek ():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.peek()==3

    stack.pop()
    assert stack.peek()==2

def test_instantiate_empty_stack():
      stack = Stack()
      assert stack.is_empty() == True
      assert stack.pop() == 'Stack is empty'
      assert stack.peek() == 'Stack is empty'



# Queue tests

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.front.value == 1
    assert queue.rear.value == 3


def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    assert queue.front.value == 2

def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1

def test_queue_is_empty():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() == True



def test_instantiate_empty_queue():
    queue = Queue()
    assert queue.front == None
    assert queue.rear == None
    assert queue.dequeue() == 'Queue is empty'
    assert queue.peek() == 'Queue is empty'