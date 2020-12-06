import math

from utils.file import read_file_content


def split(min, max, lower) -> (int, int):
    if lower:
        return (min, (math.floor( (min + max)/2) ))
    else:
        return (math.ceil( ((min + max)/2) ), max)


def find_row(inp: str):
    min = 0
    max = 127
    for x in inp:
        (min, max) = split(min, max, (x == 'F'))
    # min and max should be equal by now
    return min


def find_seat(inp: str):
    min = 0
    max = 7
    for x in inp:
        (min, max) = split(min, max, (x == 'L'))
    # min and max should be equal by now
    return min


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    maxSeatID = 0
    for line in inp:
        row = find_row(line[:7])
        seat = find_seat(line[7:])
        seatID = (row*8)+seat
        if seatID > maxSeatID:
            maxSeatID = seatID
    return maxSeatID


def solve_part2(inp: str) -> int:
    occupied = [False]*(128*8)
    inp = inp[:-1].split("\n")
    for line in inp:
        row = find_row(line[:7])
        seat = find_seat(line[7:])
        seatID = (row * 8) + seat
        occupied[seatID] = True

    for i in range(len(occupied)):
        if occupied[i] == False:
            if occupied[i-1] == True and occupied[i+2] == True:
                return i
    return -1


def solve_part1_binary(inp: str) -> int:
    inp = inp[:-1].split("\n")
    max_seat = 0
    for line in inp:
        line = line.replace('F', '0').replace('B', '1')
        line = line.replace('L', '0').replace('R', '1')
        seat_id = int(line, 2)
        if seat_id > max_seat:
            max_seat = seat_id
    return max_seat

def solve_part2_binary(inp: str) -> int:
    inp = inp[:-1].split("\n")
    occupied = [False]*(128*8)
    for line in inp:
        line = line.replace('F', '0').replace('B', '1')
        line = line.replace('L', '0').replace('R', '1')
        seat_id = int(line, 2)
        occupied[seat_id] = True

    for i in range(len(occupied)):
        if occupied[i] == False:
            if occupied[i-1] == True and occupied[i+2] == True:
                return i
    return -1


def test_part1():
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1_binary(inp)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    # There are no tests for part 2 in this case, but our answer was correct the first time, oh well.
    inp = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans2"))

    result = solve_part2_binary(inp)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


if __name__ == '__main__':

    inp = read_file_content("inputs/input")

    print(" --- Part 1 --- ")
    test_part1()
    print("Part 1 result:\t" + str(solve_part1_binary(inp)))

    print("\n --- Part 2 ---")
    test_part2()
    print("Part 2 result:\t" + str(solve_part2_binary(inp)))
