from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    m = 0.0
    b = 0
    while b < len(prices)-1:
        s = b + 1
        t = prices[b]
        while s < len(prices):
            if prices[s] > t:
                t = prices[s]
            s += 1
        p = t - prices[b]
        if p > m:
            m = p
        b += 1

    return m


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
