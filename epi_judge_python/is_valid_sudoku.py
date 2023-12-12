from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    
    for i in range(len(partial_assignment)):
        for j in range(len(partial_assignment[0])):
            cv = partial_assignment[i][j]
            if cv == 0:
                continue
            c = j + 1
            while c < len(partial_assignment[0]):
                if partial_assignment[i][c] == cv:
                    return False
                c += 1
                
    for j in range(len(partial_assignment[0])):
        for i in range(len(partial_assignment)):
            cv = partial_assignment[i][j]
            if cv == 0:
                continue
            r = i + 1
            while r < len(partial_assignment):
                if partial_assignment[r][j] == cv:
                    return False
                r += 1
    sg = set()
    for i in range(0, len(partial_assignment), 3):
        for j in range(0, len(partial_assignment[0]), 3):
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    cv = partial_assignment[r][c]
                    if cv == 0:
                        continue
                    elif cv in sg:
                        return False
                    else:
                        sg.add(cv)

            sg.clear()

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
