import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    # TODO - you fill in here.
    stack = []
    str = ''
    for i in range(len(s)):
        if s[i] == ' ':
            stack.append(str)
            stack.append(' ')
            str = ''
        elif i == len(s) - 1:
            str += s[i]
            stack.append(str)
        else:
            str += s[i]
    j = 0
    while len(stack) > 0:
        w = stack.pop()
        for i in range(len(w)):
            s[j] = w[i]
            j += 1

    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
