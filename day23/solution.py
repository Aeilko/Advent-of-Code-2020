from collections import deque

from utils.file import read_file_content


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


def solve_part2(inp: str) -> int:
    pass


def test_part1():
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(inp)
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

    print("\n --- Part 2 ---")
    test_part2()
    print("Part 2 result:\t" + str(solve_part2(inp)))
