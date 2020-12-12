from utils.file import read_file_content


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")

    (x, y) = (0, 0)
    direction = 1

    for line in inp:
        cmd = line[:1]
        num = int(line[1:])

        if cmd == "N":
            y += num
        elif cmd == "S":
            y -= num
        elif cmd == "E":
            x += num
        elif cmd == "W":
            x -= num
        elif cmd == "L" or cmd == "R":
            steps = int(4 - num/90) if cmd == "L" else int(num/90)
            direction = (direction + steps) % 4
        elif cmd == "F":
            if direction == 0:
                y += num
            elif direction == 1:
                x += num
            elif direction == 2:
                y -= num
            elif direction == 3:
                x -= num

    return abs(x) + abs(y)


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")

    (x, y) = (0, 0)
    (wx, wy) = (10, 1)

    for line in inp:
        cmd = line[:1]
        num = int(line[1:])

        if cmd == "N":
            wy += num
        elif cmd == "S":
            wy -= num
        elif cmd == "E":
            wx += num
        elif cmd == "W":
            wx -= num
        elif cmd == "L" or cmd == "R":
            steps = int(4 - num/90) if cmd == "L" else int(num/90)
            for i in range(steps):
                tmp = wx
                wx = wy
                wy = tmp * -1
        elif cmd == "F":
            x += wx * num
            y += wy * num

    return abs(x) + abs(y)


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
