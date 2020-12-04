
def list_equals(l1: list, l2: list) -> bool:

    if len(l1) != len(l2):
        return False

    for i in l1:
        if i not in l2:
            return False

    return True
