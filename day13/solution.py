import math

from utils.file import read_file_content
from utils.list import find_max


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")

    time = int(inp[0])

    busses = set()
    blist = inp[1].split(",")
    for b in blist:
        if b != 'x':
            busses.add(int(b))

    min_time = find_max(busses)
    min_bus = -1
    for b in busses:
        mod = time % b
        d_time = b - mod

        if d_time < min_time:
            min_time = d_time
            min_bus = b

    return min_time * min_bus


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")

    departs = ['x']
    bus_times = {}
    all_busses = {}
    dlist = inp[1].split(",")
    for i in range(len(dlist)):
        b = dlist[i]
        if b != 'x':
            b = int(b)
            bus_times[b] = i+1

        departs.append(b)
    max_time = len(departs)

    for id in bus_times:
        time = bus_times[id]
        first_depart = time % id
        for t in range(first_depart, max_time, id):
            if t in all_busses:
                all_busses.get(t).append(id)
            else:
                all_busses[t] = [id]

    # Find highest multiple
    max = 0
    max_t = -1
    for time in all_busses:
        multiple = math.prod(all_busses.get(time))
        if multiple > max:
            max = multiple
            max_t = time

    # Find correct moment
    t = max - max_t
    while True:
        found = True
        for id in bus_times:
            if (t + bus_times.get(id)) % id != 0:
                found = False
                break

        if found:
            break
        t += max
    return t+1


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
