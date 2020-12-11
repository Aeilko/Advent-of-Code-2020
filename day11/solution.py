from utils.file import read_file_content
from utils.list import double_deep_copy


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")

    width = len(inp[0])
    height = len(inp)
    state = [[]]*height
    for i in range(height):
        state[i] = [' ']*width

    for i in range(height):
        for j in range(width):
            state[i][j] = inp[i][j]

    old_state = []
    while state != old_state:
        old_state = double_deep_copy(state)
        for i in range(height):
            for j in range(width):
                if old_state[i][j] == '.':
                    continue

                occ = 0
                for y in range((i-1 if i > 0 else 0), (i+2 if i < height-1 else i+1)):
                    for x in range((j-1 if j > 0 else 0), (j+2 if j < width-1 else j+1)):
                        if x == j and y == i:
                            continue

                        elif old_state[y][x] == '#':
                            occ += 1

                if old_state[i][j] == 'L' and occ == 0:
                    state[i][j] = '#'
                elif old_state[i][j] == '#' and occ >= 4:
                    state[i][j] = 'L'

    r = 0
    for line in state:
        for char in line:
            if char == "#":
                r += 1
    return r


def check_direction(state: list, x: int, y: int, dir: int) -> bool:
    height = len(state)
    width = len(state[0])
    if dir == 0:
        if y == 0:
            return False
        else:
            y -= 1
    elif dir == 1:
        if y == 0 or x == width-1:
            return False
        else:
            y -= 1
            x += 1
    elif dir == 2:
        if x == width-1:
            return False
        else:
            x += 1
    elif dir == 3:
        if x == width-1 or y == height-1:
            return False
        else:
            x += 1
            y += 1
    elif dir == 4:
        if y == height-1:
            return False
        else:
            y += 1
    elif dir == 5:
        if x == 0 or y == height-1:
            return False
        else:
            x -= 1
            y += 1
    elif dir == 6:
        if x == 0:
            return False
        else:
            x -= 1
    elif dir == 7:
        if x == 0 or y == 0:
            return False
        else:
            x -= 1
            y -= 1

    if state[y][x] == 'L':
        return False
    elif state[y][x] == '#':
        return True
    else:
        return check_direction(state, x, y, dir)


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")

    width = len(inp[0])
    height = len(inp)
    state = [[]] * height
    for i in range(height):
        state[i] = [' '] * width

    for i in range(height):
        for j in range(width):
            state[i][j] = inp[i][j]

    old_state = []
    while state != old_state:
        old_state = double_deep_copy(state)
        for i in range(height):
            for j in range(width):
                if old_state[i][j] == '.':
                    continue

                occ = 0
                for x in range(8):
                    if check_direction(old_state, j, i, x):
                        occ += 1

                if old_state[i][j] == 'L' and occ == 0:
                    state[i][j] = '#'
                elif old_state[i][j] == '#' and occ >= 5:
                    state[i][j] = 'L'

    r = 0
    for line in state:
        for char in line:
            if char == "#":
                r += 1
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
