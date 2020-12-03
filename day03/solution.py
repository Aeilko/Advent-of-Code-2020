from utils.file import read_file_content


def solve_part1(inp: str) -> int:
    inp = inp.split("\n")
    height = len(inp)
    width = len(inp[0])
    x = 0
    step = 3
    trees = 0
    for i in range(1, height):
        x = (x+step) % width
        if inp[i][x] == '#':
            trees += 1
    return trees


def solve_part2(inp: str) -> int:
    inp = inp.split("\n")
    height = len(inp)
    width = len(inp[0])
    settings = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    r = 1
    for (xStep, yStep) in settings:
        x = xStep
        y = yStep
        trees = 0
        while y < height:
            if inp[y][x] == '#':
                trees += 1

            x = (x + xStep) % width
            y += yStep
        r *= trees

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
