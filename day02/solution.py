from utils.file import read_file_content


def solve_part1(input: str) -> int:
    r = 0
    input = input.split("\n")
    for line in input:
        # Parse the line
        (settings, text) = line.split(": ")
        (minmax, char) = settings.split(" ")
        (min, max) = minmax.split("-")

        c = text.count(char)
        if c >= int(min) and c <= int(max):
            r += 1

    return r


def solve_part2(input: str) -> int:
    r = 0
    input = input.split("\n")
    for line in input:
        # Parse the line
        (settings, text) = line.split(": ")
        (minmax, char) = settings.split(" ")
        (min, max) = minmax.split("-")
        min = int(min)
        max = int(max)

        if (text[min-1] == char) != (text[max-1] == char):
            r += 1

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
