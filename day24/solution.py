import re

from utils.file import read_file_content


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    active = []
    for line in inp:
        (x, y, z) = (0, 0, 0)
        moves = re.findall("([ns]?[ew])", line)
        for move in moves:
            if move == 'w':
                x -= 1
                z += 1
            elif move == 'e':
                x += 1
                z -= 1
            elif move == 'ne':
                y += 1
                z -= 1
            elif move == "sw":
                y -= 1
                z += 1
            elif move == "nw":
                y += 1
                x -= 1
            elif move == "se":
                y -= 1
                x += 1
        if (x, y, z) in active:
            active.remove((x, y, z))
        else:
            active.append((x, y, z))
    return len(active)


def find_min_max(active: dict, param: int) -> (int, int):
    min = 100000000
    max = 0
    for item in active:
        if item[param] > max:
            max = item[param]
        if item[param] < min:
            min = item[param]
    return (min, max)


def get_neighbours(x, y, z):
    r = set()
    r.add((x+1, y-1, z))
    r.add((x-1, y+1, z))
    r.add((x+1, y, z-1))
    r.add((x-1, y, z+1))
    r.add((x, y+1, z-1))
    r.add((x, y-1, z+1))
    return r


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")
    active = set()
    for line in inp:
        (x, y, z) = (0, 0, 0)
        moves = re.findall("([ns]?[ew])", line)
        for move in moves:
            if move == 'w':
                x -= 1
                z += 1
            elif move == 'e':
                x += 1
                z -= 1
            elif move == 'ne':
                y += 1
                z -= 1
            elif move == "sw":
                y -= 1
                z += 1
            elif move == "nw":
                y += 1
                x -= 1
            elif move == "se":
                y -= 1
                x += 1
        if (x, y, z) in active:
            active.remove((x, y, z))
        else:
            active.add((x, y, z))

    for _ in range(10):
        old = set(active)
        active_neighbours = {}
        for (x, y, z) in old:
            cur_n = get_neighbours(x, y, z)

            n = 0
            for (nx, ny, nz) in cur_n:
                if (nx, ny, nz) in old:
                    n += 1
                else:
                    if (nx,  ny, nz) in active_neighbours:
                        active_neighbours[(nx, ny, nz)] += 1
                    else:
                        active_neighbours[(nx, ny, nz)] = 1

            if n != 1:
                active.remove((x, y, z))

        for (x, y, z) in active_neighbours:
            if active_neighbours[(x, y, z)] == 2:
                active.add((x, y, z))
        print(len(active))

    return len(active)


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
    # print("Part 2 result:\t" + str(solve_part2(inp)))
