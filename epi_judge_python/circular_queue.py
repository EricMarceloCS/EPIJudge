from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    queue_capacity: int
    cir_queue = []

    def __init__(self, capacity: int) -> None:
        self.queue_capacity = capacity
        return

    def enqueue(self, x: int) -> None:
        self.cir_queue.append(x)
        return

    def dequeue(self) -> int:
        if len(self.cir_queue) > 0:
            return self.cir_queue.pop(0)
        return 0

    def size(self) -> int:
        return len(self.cir_queue)


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
