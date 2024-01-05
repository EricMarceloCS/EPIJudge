from test_framework import generic_test


def evaluate(expression: str) -> int:
    rpn_stack = []
    s = ""
    i = 0
    while i < len(expression):
        c = expression[i]
        if c == ",":
            rpn_stack.append(int(s))
            i += 1
            s = ""
        elif c == "*":
            num_1 = rpn_stack.pop()
            num_2 = rpn_stack.pop()
            rpn_stack.append(num_1 * num_2)
            i += 2
        elif c == "/":
            num_1 = rpn_stack.pop()
            num_2 = rpn_stack.pop()
            rpn_stack.append(num_2 // num_1)
            i += 2
        elif c == "-":
            num_1 = rpn_stack.pop()
            num_2 = rpn_stack.pop()
            rpn_stack.append(num_2 - num_1)
            i += 2
        elif c == "+":
            num_1 = rpn_stack.pop()
            num_2 = rpn_stack.pop()
            rpn_stack.append(num_1 + num_2)
            i += 2
        else:
            s += c
            i += 1

    if s != '':
        rpn_stack.append(int(s))

    return rpn_stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
