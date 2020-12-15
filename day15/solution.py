from utils.file import read_file_content


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split(",")
    prev_number = -1
    last_spoken = {}
    turn = 1
    for x in inp:
        last_spoken[int(x)] = turn
        prev_number = int(x)
        turn += 1

    while turn <= 2020:
        res = 0
        if prev_number in last_spoken:
            res = (turn-1) - last_spoken[prev_number]

        last_spoken[prev_number] = turn-1
        prev_number = res

        turn += 1

    return prev_number


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split(",")
    prev_number = -1
    last_spoken = {}
    turn = 1
    for x in inp:
        last_spoken[int(x)] = turn
        prev_number = int(x)
        turn += 1

    while turn <= 30000000:
        res = 0
        if prev_number in last_spoken:
            res = (turn - 1) - last_spoken[prev_number]

        last_spoken[prev_number] = turn - 1
        prev_number = res

        turn += 1

    return prev_number


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
