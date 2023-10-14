import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    x, y, w, h = 0, 0, 0, 0
    if (r2.x > r1.x and r2.x > r1.x + r1.width) or (r1.x > r2.x and r1.x > r2.x + r2.width):
        return Rect(0, 0, -1, -1)
    elif (r2.y > r1.y and r2.y > r1.y + r1.height) or (r1.y > r2.y and r1.y > r2.y + r2.height):
        return Rect(0, 0, -1, -1)

    if r1.x <= r2.x:
        x = r2.x
        if (r2.x + r2.width) <= (r1.x + r1.width):
            w = r2.width
        else:
            w = (r1.x + r1.width) - r2.x
    else:
        x = r1.x
        if (r1.x + r1.width) <= (r2.x + r2.width):
            w = r1.width
        else:
            w = (r2.x + r2.width) - r1.x

    if r1.y >= r2.y:
        y = r1.y
        if (r1.y + r1.height) <= (r2.y + r2.height):
            h = r1.height
        else:
            h = (r2.y + r2.height) - r1.y
    else:
        y = r2.y
        if (r2.y + r2.height) <= (r1.y + r1.height):
            h = r2.height
        else:
            h = (r1.y + r1.height) - r2.y

    return Rect(x, y, w, h)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
