import sys


def list_equals(l1: list, l2: list) -> bool:

    if len(l1) != len(l2):
        return False

    for i in l1:
        if i not in l2:
            return False

    return True


def find_min(l: iter) -> int:
    min = sys.maxsize
    for x in l:
        if x < min:
            min = x
    return min


def find_max(l: iter) -> int:
    # For some reason sys.maxsize+1 does not overflow to the min value?
    max = sys.maxsize*-1
    for x in l:
        if x > max:
            max = x
    return max



