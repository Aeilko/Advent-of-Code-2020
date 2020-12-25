from utils.file import read_file_content


def solve_part1(inp: str) -> int:
    (pk1, pk2) = [int(x) for x in inp[:-1].split("\n")]

    sn = 1
    r = 1
    while True:
        sn = (sn * 7) % 20201227
        r = (r * pk2) % 20201227
        if sn == pk1:
            break

    return r


def test_part1():
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(inp)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


if __name__ == '__main__':
    inp = read_file_content("inputs/input")

    print(" --- Part 1 --- ")
    test_part1()
    print("Part 1 result:\t" + str(solve_part1(inp)))
