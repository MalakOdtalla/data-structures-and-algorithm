from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue

def test_enqueue():
  queue = PseudoQueue()
  queue.enqueue(1)
  queue.enqueue(2)
  assert  queue.firststack.top.value == 2


def test_dequeue():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.secondstack.top.value == 3
    assert queue.dequeue() == 1
