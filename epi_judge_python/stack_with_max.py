from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    s = []

    def empty(self) -> bool:
        return len(self.s) == 0

    def max(self) -> int:
        m = self.s[0]
        for i in range(1, len(self.s)):
            if self.s[i] > m:
                m = self.s[i]
        return m

    def pop(self) -> int:
        if not self.empty():
            return self.s.pop()
        return None

    def push(self, x: int) -> None:
        self.s.append(x)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
