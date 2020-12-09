import sys

def list_equals(l1: list, l2: list) -> bool:

    if len(l1) != len(l2):
        return False

    for i in l1:
        if i not in l2:
            return False

    return True


def list_min(l: iter):
    min = sys.maxsize
    for x in l:
        if x < min:
            min = x
    return min


def list_max(l: iter):
    # For some reason sys.maxsize+1 does not overflow to the min value?
    max = sys.maxsize*-1
    for x in l:
        if x > max:
            max = x
    return max



