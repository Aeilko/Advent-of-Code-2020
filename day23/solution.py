from collections import deque

from utils.file import read_file_content
from utils.linked_list import LinkedList


def solve_part1(inp: str) -> int:
    cups = []
    current = 0
    for d in inp[:-1]:
        cups.append(int(d))

    for _ in range(100):
        picked = []
        for _ in range(3):
            if current == len(cups)-1:
                picked.append(cups.pop(0))
                current -= 1
            else:
                picked.append(cups.pop(current+1))

        destination = cups[current]-1
        while destination not in cups:
            destination -= 1
            if destination < 1:
                destination = 9

        d_index = cups.index(destination)
        for x in range(3):
            cups.insert(d_index+x+1, picked[x])
        if d_index < current:
            current += 3

        current = (current+1) % 9

    one_index = cups.index(1)
    return int("".join([str(x) for x in cups[one_index+1:]]) + "".join([str(x) for x in cups[:one_index]]))


def solve_part1_ll(inp: str) -> int:
    cups = []
    for d in inp[:-1]:
        cups.append(int(d))

    llist = LinkedList(cups)
    current = llist.values[cups[0]]
    # Create a circle in the linked list
    llist.values[cups[8]].next = current

    for _ in range(100):
        # for _ in range(10):
        tmp = current
        picked = []
        for _ in range(3):
            tmp = tmp.next
            picked.append(tmp)
        current.next = picked[2].next

        destination = current.val - 1
        while destination in picked or destination < 1:
            destination -= 1
            if destination < 1:
                destination = 9

        picked[2].next = llist.values[destination].next
        llist.values[destination].next = picked[0]

        current = current.next

    node = llist.values[1]
    r = ""
    for _ in range(8):
        node = node.next
        r += str(node.val)
    return int(r)



def solve_part2(inp: str) -> int:
    cups = []
    for d in inp[:-1]:
        cups.append(int(d))
    for x in range(len(cups)+1, 1000001):
        cups.append(x)

    llist = LinkedList(cups)
    current = llist.values[cups[0]]
    # Create a circle in the linked list
    llist.values[1000000].next = current

    for _ in range(10000000):
        tmp = current
        picked = []
        for _ in range(3):
            tmp = tmp.next
            picked.append(tmp)
        current.next = picked[2].next

        destination = current.val - 1
        while destination in picked or destination < 1:
            destination -= 1
            if destination < 1:
                destination = 1000000

        picked[2].next = llist.values[destination].next
        llist.values[destination].next = picked[0]

        current = current.next

    node_1 = llist.values[1]
    return node_1.next.val * node_1.next.next.val


def test_part1():
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(inp)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part1_ll():
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1_ll(inp)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans2"))

    result = solve_part2(inp)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


if __name__ == '__main__':
    inp = read_file_content("inputs/input")

    print(" --- Part 1 --- ")
    test_part1()
    print("Part 1 result:\t" + str(solve_part1(inp)))

    print("\n --- Part 1 (Linked List) --- ")
    test_part1_ll()
    print("Part 1 result:\t" + str(solve_part1_ll(inp)))

    print("\n --- Part 2 ---")
    test_part2()
    print("Part 2 result:\t" + str(solve_part2(inp)))
