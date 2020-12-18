import re

from utils.file import read_file_content


def evaluate_1(inp: str) -> int:
    while "(" in inp:
        sub = re.findall("\(([\d+* ]+)\)", inp)
        for s in sub:
            val = evaluate_1(s)
            inp = inp.replace("(" + s + ")", str(val))

    items = inp.split(" ")
    r = int(items[0])
    for i in range(1, len(items), 2):
        if items[i] == '*':
            r *= int(items[i+1])
        elif items[i] == "+":
            r += int(items[i+1])
    return r


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    r = 0
    for line in inp:
        r += evaluate_1(line)
    return r


def evaluate_2(inp: str) -> int:
    while "(" in inp:
        sub = re.findall("\(([\d+* ]+)\)", inp)
        for s in sub:
            val = evaluate_2(s)
            inp = inp.replace("(" + s + ")", str(val))

    while "+" in inp:
        sub = re.search("\d+ \+ \d+", inp)
        items = sub.group().split(" ")
        val = int(items[0])+int(items[2])
        # Replace on index, not using replace() since this would break on replacing 1 + 1 on: 1 + 1 + 21 + 1
        inp = inp[:sub.start()] + str(val) + inp[sub.end():]

    items = inp.split(" ")
    r = int(items[0])
    for i in range(1, len(items), 2):
        if items[i] == '*':
            r *= int(items[i+1])
        elif items[i] == "+":
            r += int(items[i+1])
    return r


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")
    r = 0
    for line in inp:
        r += evaluate_2(line)
    return r


def test_part1():
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(inp)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    # There are no tests for part 2 in this case, but our answer was correct the first time, oh well.
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
