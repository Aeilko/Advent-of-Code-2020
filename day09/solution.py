from utils.file import read_file_content
from utils.list import list_min, list_max


def solve_part1(inp: str, steps=25) -> int:
    inp = inp[:-1].split("\n")
    queue = []
    r = -1
    for line in inp:
        val = int(line)
        if len(queue) < steps:
            queue.append(val)
        else:
            # print(str(val) + ": " + str(queue))
            found = False
            for x in queue:
                rest = val-x
                if rest != val and rest in queue:
                    found = True

            if not found:
                r = val
                break

            queue.pop(0)
            queue.append(val)
    return r


def solve_part2(inp: str, steps=25) -> int:
    target = solve_part1(inp, steps)
    inp = inp[:-1].split("\n")

    minI = -1
    maxI = -1
    for i in range(len(inp)):
        val = int(inp[i])
        j = i+1
        while val < target:
            val += int(inp[j])
            if val == target:
                minI = i
                maxI = j
            j += 1

        if minI != -1:
            break

    vals = [int(x) for x in inp[minI:maxI+1]]
    min = list_min(vals)
    max = list_max(vals)

    return min+max


def test_part1():
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(inp, 5)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    # There are no tests for part 2 in this case, but our answer was correct the first time, oh well.
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans2"))

    result = solve_part2(inp, 5)
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
