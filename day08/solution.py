import re

from utils.file import read_file_content


def compute(inp: list, return_all=False):
    pointer = 0
    acc = 0
    visited = set()
    while pointer not in visited:
        visited.add(pointer)
        (cmd, val) = re.match("(nop|acc|jmp) ([\+-]\d+)", inp[pointer]).groups()
        val = int(val)
        # print(cmd + ' ' + str(val))
        if cmd == 'nop':
            pointer += 1
        elif cmd == "acc":
            acc += val
            pointer += 1
        elif cmd == "jmp":
            pointer += val

        if pointer >= len(inp):
            break

    if return_all:
        return (pointer, acc, visited)
    else:
        return acc


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    return compute(inp)


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")
    (pointer, acc, targets) = compute(inp, True)
    r = -1
    for i in targets:
        og = inp[i]
        if og[:3] == "jmp":
            inp[i] = "nop" + og[3:]
        elif og[:3] == "nop":
            inp[i] = "jmp" + og[3:]

        (p, a, v) = compute(inp, True)
        if p == len(inp):
            r = a
            break
        else:
            inp[i] = og
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
