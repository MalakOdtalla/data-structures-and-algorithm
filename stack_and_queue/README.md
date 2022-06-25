# Stacks and Queues

- Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle.

- Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.


## Challenge

Write queue and stack classes with their methods


## Approach & Efficiency

- Big O :  is O(1) for all methods that used in Stacks and queues. 

## API

### Stack methods:

- push() : Adds a new node at the top of the stack
- pop(): Deletes the top most element of the stack
- Peek() : returns the value of the top Node in the stack.
- Is_empty : returns true when stack is empty otherwise returns false.

### Queue methods:
- Enqueue : returns Nodes or items that are added to the queue.
- Dequeue : returns Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.
- Peek : returns the value of the front Node in the queue. If called when the queue is empty an exception will be raised.
- Is_empty - returns true when queue is empty otherwise returns false.