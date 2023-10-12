from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    m_1 = 1
    m_2 = 2

    while (x & m_1 and x & m_2) or (x & m_1 == 0 and x & m_2 == 0):
        m_1 <<= 1
        m_2 <<= 1

    if x & m_1 and x & m_2 == 0:
        x ^= m_1
        x |= m_2
    elif x & m_1 == 0 and x & m_2:
        x |= m_1
        x ^= m_2

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
