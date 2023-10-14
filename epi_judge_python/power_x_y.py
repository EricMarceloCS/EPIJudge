from test_framework import generic_test


def power(x: float, y: int) -> float:
    r = 1
    if y > 0:
        for i in range(y):
            r *= x
    else:
        y = -y
        for i in range(y):
            r /= x
    return r


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
