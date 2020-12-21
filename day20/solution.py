import math
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

    # Find the amount of unmatched borders per tile
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


def rotate_tile(inp: list, times: int) -> list:
    for _ in range(times):
        outp = ["." * len(inp) for _ in range(len(inp))]
        for x in range(len(inp[0])):
            new_line = ""
            for y in range(len(inp)-1, -1, -1):
                new_line += inp[y][x]
            outp[x] = new_line
        inp = outp
    return inp


def flip_tile(inp: list, dim: chr) -> list:
    outp = [None]*len(inp)
    if dim == 'v':
        for y in range(len(inp)):
            outp[y] = inp[y][::-1]
    elif dim == 'h':
        for y in range(len(inp)):
            outp[y] = inp[len(inp)-y-1]

    return outp


def get_border_tile(border: str, dir: chr, borders: dict, tiles: dict, excludes: set) -> (int, list):
    poss_tiles = borders.get(border)
    if poss_tiles is None:
        poss_tiles = borders.get(border[::-1])

    tile =[]

    for tile_id in poss_tiles:
        if tile_id in excludes:
            continue

        tile = tiles.get(tile_id)
        found = False
        while not found:
            if dir == 't':
                cur_border = tile[0]
            elif dir == 'r':
                cur_border = "".join([l[len(l)-1] for l in tile])
            elif dir == 'b':
                cur_border = tile[len(tile)-1]
            elif dir == 'l':
                cur_border = "".join([l[0] for l in tile])

            if cur_border == border or cur_border[::-1] == border:
                if cur_border[::-1] == border:
                    if dir in ['t', 'b']:
                        tile = flip_tile(tile, 'v')
                    else:
                        tile = flip_tile(tile, 'h')
                found = True
                break

            tile = rotate_tile(tile, 1)

        if found:
            break
    return (tile_id, tile)


def find_dragons(inp: list) -> int:
    r = 0
    for y in range(1, len(inp)-1):
        for x in range(0, len(inp)-20):
            signs = [inp[y][x], inp[y+1][x+1], inp[y+1][x+4], inp[y][x+5], inp[y][x+6], inp[y+1][x+7], inp[y+1][x+10], inp[y][x+11], inp[y][x+12], inp[y+1][x+13], inp[y+1][x+16], inp[y][x+17], inp[y-1][x+18], inp[y][x+18], inp[y][x+19]]
            if signs.count("#") == 15:
                r += 1
    return r


def solve_part2(inp: str) -> int:
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

    # Find the amount of unmatched borders per tile
    counts = {}
    for b in borders:
        if len(borders.get(b)) == 1:
            for id in borders.get(b):
                if id in counts:
                    counts[id] += 1
                else:
                    counts[id] = 1

    # Start from a corner piece (2 unmatched borders) and add all neighbouring pieces from there on
    corners = set()
    edges = set()
    for c in counts:
        if counts.get(c) == 2:
            corners.add(c)
        elif counts.get(c) == 1:
            edges.add(c)

    # Orientate the top left tile correctly
    top_left_id = corners.pop()
    top_left_tile = tiles.get(top_left_id)
    top = (borders.get(top_left_tile[0]) is None or len(borders.get(top_left_tile[0])) == 2)
    bot = (borders.get(top_left_tile[len(top_left_tile) - 1]) is None or len(borders.get(top_left_tile[len(top_left_tile) - 1])) == 2)
    left = (borders.get("".join([l[0] for l in top_left_tile])) is None or len(borders.get("".join([l[0] for l in top_left_tile]))) == 2)
    right = (borders.get("".join([l[len(l) - 1] for l in top_left_tile])) is None or len(borders.get("".join([l[len(l) - 1] for l in top_left_tile]))) == 2)
    if top and right:
        top_left_tile = rotate_tile(top_left_tile, 1)
    elif left and top:
        top_left_tile = rotate_tile(top_left_tile, 2)
    elif bot and left:
        top_left_tile = rotate_tile(top_left_tile, 3)

    # Connect all pieces to the start tile
    size = int(math.sqrt(len(tiles)))
    cur_tile = top_left_tile
    cur_id = top_left_id
    exludes = {cur_id}
    image = ["" for _ in range(size*(len(cur_tile)-2))]
    first = True
    for y in range(size):
        if first:
            first = False
            bot_border = cur_tile[len(cur_tile)-1]
        else:
            (cur_id, cur_tile) = get_border_tile(bot_border, 't', borders, tiles, exludes)
            exludes.add(cur_id)
            bot_border = cur_tile[len(cur_tile)-1]

        for i in range(len(cur_tile)-2):
            image[y*(len(cur_tile)-2)+i] += cur_tile[i+1][1:-1]

        for _ in range(size-1):
            (cur_id, cur_tile) = get_border_tile("".join([l[len(l) - 1] for l in cur_tile]), 'l', borders, tiles, exludes)
            exludes.add(cur_id)
            for i in range(len(cur_tile)-2):
                image[y*(len(cur_tile)-2)+i] += cur_tile[i+1][1:-1]

    # Search for dragons in different orientations
    found = False
    dragons = -1
    for _ in range(2):
        image = rotate_tile(image, 1)
        for _ in range(2):
            image = flip_tile(image, 'v')
            for _ in range(2):
                image = flip_tile(image, 'h')
                dragons = find_dragons(image)
                if dragons != 0:
                    found = True
                    break
            if found:
                break
        if found:
            break

    # Count the non dragon fields
    r = 0
    for line in image:
        r += line.count("#")
    r -= dragons*15

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
