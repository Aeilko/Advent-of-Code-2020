from utils.file import read_file_content


# I don't know what i have been doing for part 1. I came up with something, and just decided to stick with it.
# Even though i figured it made no sense, i thought i was committed at that point (its only part 1 right?)


def print_state(state: dict):
    for z in state:
        if z == 'dim':
            continue
        for y in range(len(state.get(z))):
            line = ""
            for val in state.get(z)[y]:
                if val:
                    line += "#"
                else:
                    line += "."
            print(line)
        print()


def find_active_old_neighbors(x: int, y: int, z: int, old_state: dict) -> int:
    dim = old_state['dim']+2
    zs = int(len(old_state)/2)
    zmin = z-1 if z > (zs*-1)+1 else (zs*-1)+1
    zmax = z+1 if z < zs-1 else zs-1
    xmin = x-1 if x > 1 else 1
    xmax = x+1 if x+2 < dim else dim-2
    ymin = y-1 if y > 1 else 1
    ymax = y+1 if y+2 < dim else dim-2
    r = 0
    for nz in range(zmin, zmax+1):
        for ny in range(ymin, ymax+1):
            for nx in range(xmin, xmax+1):
                if nz == z and nx == x and ny == y:
                    continue
                if old_state.get(nz)[ny-1][nx-1]:
                    r += 1
    return r


def perform_cycle(state: dict) -> dict:
    zs = int(len(state)/2)
    old_state = state.copy()
    state = {}
    dim = old_state['dim'] + 2
    state['dim'] = dim

    for z in range(zs*-1, zs+1):
        field = [[False]*dim for _ in range(dim)]
        for y in range(dim):
            for x in range(dim):

                neighbours = find_active_old_neighbors(x, y, z, old_state)
                val = False
                if 0 < x < dim-1 and 0 < y < dim-1 and zs*-1 < z < zs:
                    val = old_state.get(z)[y-1][x-1]

                if val and (neighbours < 2 or neighbours > 3):
                    val = False
                elif not val and neighbours == 3:
                    val = True
                field[y][x] = val
        state[z] = field

    return state


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    dimension = len(inp)
    state = {}
    field = [[False]*dimension for _ in range(dimension)]
    for y in range(dimension):
        for x in range(dimension):
            if inp[y][x] == '#':
                field[y][x] = True
    state['dim'] = dimension
    state[0] = field

    for x in range(6):
        state = perform_cycle(state)

    r = 0
    for z in state:
        if z == 'dim':
            continue

        z = state.get(z)
        for y in z:
            for x in y:
                if x:
                    r += 1
    return r


def expand(state: list) -> list:
    w = len(state)+2
    z = len(state[0])+2
    y = len(state[0][0])+2
    x = len(state[0][0][0])+2

    new = [[[[False]*x for _ in range(y)] for _ in range(z)] for _ in range(w)]
    for w in range(len(state)):
        for z in range(len(state[w])):
            for y in range(len(state[w][z])):
                for x in range(len(state[w][z][y])):
                    new[w+1][z+1][y+1][x+1] = state[w][z][y][x]

    return new


def new_neighbours(w: int, z: int, y: int, x: int, state: list) -> int:
    r = 0
    for w_r in range(w-1, w+2):
        if w_r < 0 or w_r >= len(state):
            continue
        for z_r in range(z-1, z+2):
            if z_r < 0 or z_r >= len(state[w_r]):
                continue
            for y_r in range(y-1, y+2):
                if y_r < 0 or y_r >= len(state[w_r][z_r]):
                    continue
                for x_r in range(x-1, x+2):
                    if x_r < 0 or x_r >= len(state[w_r][z_r][y_r]):
                        continue
                    if state[w_r][z_r][y_r][x_r] and not (w_r == w and z_r == z and y_r == y and x_r == x):
                        r += 1
    return r


def new_cycle(state: list) -> list:
    old_state = expand(state)
    state = [[[[False]*len(old_state[0][0][0]) for _ in range(len(old_state[0][0]))] for _ in range(len(old_state[0]))] for _ in range(len(old_state))]

    for w in range(len(state)):
        for z in range(len(state[w])):
            for y in range(len(state[w][z])):
                for x in range(len(state[w][z][y])):
                    n = new_neighbours(w, z, y, x, old_state)
                    val = old_state[w][z][y][x]
                    if val and (n < 2 or n > 3):
                        val = False
                    elif not val and n == 3:
                        val = True
                    state[w][z][y][x] = val

    return state


def solve_part2(inp: str) -> int:
    # We are using coords in the following format: (w, z, y, x)
    inp = inp[:-1].split("\n")
    z_val = []
    for y in range(len(inp)):
        y_val = []
        for x in range(len(inp[y])):
            y_val.append(inp[y][x] == '#')
        z_val.append(y_val)
    state = [[z_val]]

    for _ in range(6):
        state = new_cycle(state)

    r = 0
    for w in state:
        for z in w:
            for y in z:
                for x in y:
                    if x:
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
