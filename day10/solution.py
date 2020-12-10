from utils.file import read_file_content
from utils.list import find_max


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    jolts = [0]
    for line in inp:
        jolts.append(int(line))
    jolts.append(find_max(jolts)+3)
    jolts.sort()

    diffs = {
        1: 0,
        2: 0,
        3: 0
    }

    for i in range(1, len(jolts)):
        diff = jolts[i]-jolts[i-1]
        diffs[diff] = diffs.get(diff)+1

    return diffs[1]*diffs[3]


def poss_from(inp: list, index: int, known: dict) -> dict:
    r = 0
    diff = inp[index+1]-inp[index]
    if diff == 3:
        r = known.get(inp[index+1])
    elif diff == 2 and index < len(inp)-2:
        r += known.get(inp[index+1])
        n_diff = inp[index+2]-inp[index]
        if n_diff == 3:
            r += known.get(inp[index+2])
    elif diff == 1:
        r += known.get(inp[index+1])
        n_diff = inp[index+2]-inp[index] if index < len(inp)-2 else -1
        nn_diff = inp[index+3]-inp[index] if index < len(inp)-3 else -1
        if n_diff == 2:
            r += known.get(inp[index+2])
            if nn_diff == 3:
                r += known.get(inp[index+3])
        elif n_diff == 3:
            r += known.get(inp[index+2])

    known[inp[index]] = r

    return known


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")
    jolts = [0]
    for line in inp:
        jolts.append(int(line))
    jolts.append(find_max(jolts) + 3)
    jolts.sort()

    known = {
        jolts[len(jolts)-1]: 1
    }
    for i in range(len(jolts)-2, -1, -1):
        known = poss_from(jolts, i, known)
    return known[0]


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
