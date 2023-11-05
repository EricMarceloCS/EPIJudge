import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    rp = len(s) - 1
    lp = rp - size
    while lp >= 0:
        if s[lp] == 'b':
            lp -= 1
        elif s[lp] == 'a':
            s[rp] = 'd'
            s[rp-1] = 'd'
            rp -= 2
            lp -= 1
        else:
            s[rp] = s[lp]
            lp -= 1
            rp -= 1

    for i in range(rp, -1, -1):
        s.pop(i)

    return len(s)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
