import re

from utils.file import read_file_content


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    is_contained_by = {}
    for line in inp:
        (bag, value) = line.split(" bags contain", 1)
        colors = set(re.findall("\d+ ([\w ]+) bags?", value))

        for c in colors:
            if c not in is_contained_by:
                is_contained_by[c] = set([bag])
            else:
                is_contained_by.get(c).add(bag)

    queue = ["shiny gold"]
    r = set()
    while len(queue) > 0:
        bag = queue.pop()
        r.add(bag)
        if bag in is_contained_by:
            for c in is_contained_by.get(bag):
                if c not in r and c not in queue:
                    queue.append(c)
    return len(r)-1


def part2_count(bag: str, contains: dict, known_bags: dict) -> int:
    if bag in known_bags:
        return known_bags.get(bag)
    else:
        r = 0
        sub_bags = contains.get(bag)
        for (amount, b) in sub_bags:
            r += int(amount) + int(amount) * part2_count(b, contains, known_bags)
        known_bags[bag] = r
        return r


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")
    contains = {}
    for line in inp:
        (bag, value) = line.split(" bags contain", 1)
        colors = set(re.findall("(\d+) ([\w ]+) bags?", value))

        contains[bag] = colors

    return part2_count("shiny gold", contains, {})


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
