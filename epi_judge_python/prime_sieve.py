from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    p: List = [False, False]
    r: List = []
    for i in range(2, n + 1):
        p.append(True)

    for i in range(n + 1):
        if not p[i]:
            continue;
        j = i + i
        while j <= n:
            p[j] = False
            j += i

    for i in range(len(p)):
        if p[i]:
            r.append(i)
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
