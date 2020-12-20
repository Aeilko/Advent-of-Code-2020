import re

from utils.file import read_file_content


def get_borders(tile: list):
    borders = {}
    b = list()
    b.append(tile[0])
    b.append(tile[len(tile) - 1])
    b.append("".join([l[0] for l in tile]))
    b.append("".join([l[len(l) - 1] for l in tile]))
    for border in b:
        if border in borders:
            borders.get(border).add(tile)
        else:
            borders[border] = set(tile)
    return borders


def solve_part1(inp: str) -> int:
    tiles_inp = inp[:-1].split("\n\n")
    # Parse input
    tiles = {}
    for tile in tiles_inp:
        tile = tile.split("\n")
        id = int(re.search("Tile (\d+):", tile[0]).groups()[0])
        tiles[id] = tile[1:]

    # Get possible borders
    borders = {}
    for t in tiles:
        tile = tiles[t]
        b_list = get_borders(tile)
        for b in b_list:
            if b in borders:
                borders.get(b).add(t)
            elif b[::-1] in borders:
                borders.get(b[::-1]).add(t)
            else:
                borders[b] = {t}

    # Find the amount of unmatched borders
    counts = {}
    for b in borders:
        if len(borders.get(b)) == 1:
            for id in borders.get(b):
                if id in counts:
                    counts[id] += 1
                else:
                    counts[id] = 1

    # Tiles with 2 unmatched borders are corners
    r = 1
    for c in counts:
        if counts.get(c) == 2:
            r *= c
    return r
    

def solve_part2(inp: str) -> int:
    pass


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
