import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    if len(A) == 1:
        return 1
    begin = []
    end = []
    count = 0
    max_simultaneous_events = 0

    for e in A:
        begin.append(e.start)
        end.append(e.finish)

    begin.sort()
    end.sort()

    b = begin.pop(0)
    e = end.pop(0)
    while begin or end:
        try:
            if b <= e:
                count += 1
                if count > max_simultaneous_events:
                    max_simultaneous_events = count
                b = begin.pop(0)
            else:
                count -= 1
                e = end.pop(0)
        except IndexError:
            break

    return max_simultaneous_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
