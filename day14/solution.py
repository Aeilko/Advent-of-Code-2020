from utils.file import read_file_content


to_bin = lambda x: format(x, 'b').zfill(36)


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    mask = {}
    memory = {}
    for line in inp:
        (cmd, val) = line.split(" = ")
        if cmd == 'mask':
            mask = {}
            for i in range(len(val)):
                if val[i] != 'X':
                    mask[i] = val[i]
        else:
            bits = to_bin(int(val))
            for i in range(len(bits)):
                if i in mask:
                    bits = bits[0:i] + mask[i] + bits[i+1:]
            index = int(cmd[4:-1])
            memory[index] = bits

    r = 0
    for x in memory:
        r += int(memory[x], 2)
    return r


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")
    mask = {}
    memory = {}
    for line in inp:
        (cmd, val) = line.split(" = ")
        if cmd == 'mask':
            mask = val
        else:
            index = int(cmd[4:-1])
            bits = to_bin(index)
            indices = [""]
            for i in range(len(bits)):
                if mask[i] == '0':
                    indices = [x + bits[i] for x in indices]
                elif mask[i] == '1':
                    indices = [x + '1' for x in indices]
                elif mask[i] == 'X':
                    # indices = [x + str(y) for x in indices for y in range(2)]
                    indices = [item for x in indices for item in [x + '0', x + '1']]

            for i in indices:
                i = int(i, 2)
                memory[i] = int(val)

    r = 0
    for x in memory:
        r += memory[x]
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
