from utils.file import read_file_content


def solve_part1(input: str) -> int:
    r = 0
    input = input.split("\n")
    for line in input:
        # Parse the line
        (settings, text) = line.split(": ")
        (minmax, char) = settings.split(" ")
        (min, max) = [int(x) for x in minmax.split("-")]

        c = text.count(char)
        if c >= min and c <= max:
            r += 1

    return r


def solve_part2(input: str) -> int:
    r = 0
    input = input.split("\n")
    for line in input:
        # Parse the line
        (settings, text) = line.split(": ")
        (minmax, char) = settings.split(" ")
        (i1, i2) = [int(x)-1 for x in minmax.split("-")]

        if (text[i1] == char) != (text[i2] == char):
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
