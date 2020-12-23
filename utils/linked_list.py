
class LinkedList:
    def __init__(self, data: list):
        # Create the list of nodes
        self.list = [Node(x) for x in data]

        # Link nodes
        for i in range(len(self.list)-1):
            self.list[i].next = self.list[i+1]

        # Create a list of values for efficient search
        self.values = {n.val: n for n in self.list}


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    def __eq__(self, other):
        return other == self.val
