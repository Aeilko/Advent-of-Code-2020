from utils.file import read_file_content


def solve_part1(input: str) -> int:
    input = input.split("\n")
    nums = set()
    r = 0
    for i in input:
        val = int(i)
        res = 2020-val
        if res in nums:
            r = val*res
        else:
            nums.add(val)
    return r


def solve_part2(input: str) -> int:
    input = input.split("\n")
    nums = set()
    r = 0
    found = False
    for i in input:
        val = int(i)
        res = 2020-val
        for n in nums:
            res2 = res-n
            if res2 != n and res2 > 0 and res2 in nums:
                r = val*n*res2
                found = True
                break

        nums.add(val)

        if found:
            break

    return r


def test_part1():
    input = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(input)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    input = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans2"))

    result = solve_part2(input)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


if __name__ == '__main__':

    input = read_file_content("inputs/input")

    print(" --- Part 1 --- ")
    test_part1()
    print("Part 1 result:\t" + str(solve_part1(input)))

    print("\n --- Part 2 ---")
    test_part2()
    print("Part 2 result:\t" + str(solve_part2(input)))
