import re

from utils.file import read_file_content
from utils.list import list_equals


def solve_part1(inp: str) -> int:
    inp = inp.split("\n")
    requiredAtts = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    curAtts = []
    r = 0
    for line in inp:
        if line == "":
            # Last line of this passport
            if list_equals(curAtts, requiredAtts):
                r += 1
            curAtts = []
        else:
            atts = [tuple(atts.split(":")) for atts in line.split(" ")]
            for (key, value) in atts:
                if key != 'cid':
                    curAtts.append(key)

    return r


def solve_part2(inp: str) -> int:
    inp = inp.split("\n")
    requiredAtts = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    curAtts = []
    passDenied = False
    eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    r = 0
    for line in inp:
        if passDenied:
            continue

        if line == "":
            # Last line of this passport
            if list_equals(curAtts, requiredAtts):
                r += 1
            curAtts = []
            passDenied = False
        else:
            atts = [tuple(atts.split(":")) for atts in line.split(" ")]
            for (key, value) in atts:
                if key == "byr":
                    if 1920 <= int(value) <= 2002:
                        curAtts.append(key)
                elif key == "iyr":
                    if 2010 <= int(value) <= 2020:
                        curAtts.append(key)
                elif key == "eyr":
                    if 2020 <= int(value) <= 2030:
                        curAtts.append(key)
                elif key == "hgt":
                    type = value[-2:]
                    if type == "in" or type == "cm":
                        size = int(value[:-2])
                        if (type == "in" and 59 <= size <= 76) or (type == "cm" and 150 <= size <= 193):
                            curAtts.append(key)
                elif key == "hcl":
                    if re.search("^#[0-9a-f]{6}$", value):
                        curAtts.append(key)
                elif key == "ecl" and value in eyeColors:
                    curAtts.append(key)
                elif key == "pid":
                    if re.search("^\d{9}$", value):
                        curAtts.append(key)

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
