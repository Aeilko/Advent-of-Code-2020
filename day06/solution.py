import string

from utils.file import read_file_content


def solve_part1(inp: str) -> int:
    # Remove last newline
    inp = inp[:-1].split("\n\n")
    r = 0
    for group in inp:
        s = set()
        group = group.split("\n")
        for line in group:
            for char in line:
                s.add(char)
        r += len(s)
    return r


def solve_part2(inp: str) -> int:
    # Remove last newline
    inp = inp[:-1].split("\n\n")
    r = 0
    for group in inp:
        group_set = set(string.ascii_lowercase)
        group = group.split("\n")
        for line in group:
            user_set = set(string.ascii_lowercase)
            for char in line:
                user_set.remove(char)
            group_set = group_set-user_set
        r += len(group_set)
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
