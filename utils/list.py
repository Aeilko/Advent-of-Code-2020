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


def deep_copy(l: list) -> list:
    r = [None] * len(l)
    for i in range(len(l)):
        r[i] = l[i]
    return r


def double_deep_copy(l: list) -> list:
    r = [None] * len(l)
    for i in range(len(l)):
        r[i] = [None] * len(l[i])
        for j in range(len(l[i])):
            r[i][j] = l[i][j]
    return r


def generic_deep_copy(state: list) -> list:
    r = []
    for x in state:
        if type(x) == "list":
            r.append(generic_deep_copy(x))
        else:
            r.append(x)
    return r

