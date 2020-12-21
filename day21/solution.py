import re

from utils.file import read_file_content


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n")
    ingredients = set()
    allergens = {}
    occurences = {}
    for line in inp:
        (ingredient, allergen) = re.search("([\w+ ]+)+ \(contains (\w+[, \w+]+)\)", line).groups()
        ingrs = set(ingredient.split(" "))
        allers = allergen.split(", ")

        for i in ingrs:
            ingredients.add(i)
            if i in occurences:
                occurences[i] = occurences.get(i) + 1
            else:
                occurences[i] = 1

        for a in allers:
            if a in allergens:
                allergens.get(a).append(ingrs)
            else:
                allergens[a] = [ingrs]

    impossible = ingredients
    for a in allergens:
        poss = set(ingredients)
        for i in allergens.get(a):
            poss = poss.intersection(i)
        for p in poss:
            impossible.remove(p)

    r = 0
    for i in impossible:
        r += occurences.get(i)
    return r


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n")
    ingredients = set()
    allergens = {}
    for line in inp:
        (ingredient, allergen) = re.search("([\w+ ]+)+ \(contains (\w+[, \w+]+)\)", line).groups()
        ingrs = set(ingredient.split(" "))
        allers = allergen.split(", ")

        for i in ingrs:
            ingredients.add(i)

        for a in allers:
            if a in allergens:
                allergens.get(a).append(ingrs)
            else:
                allergens[a] = [ingrs]

    found = set()
    translation = {}
    while len(found) != len(allergens):
        for a in allergens:
            poss = set(ingredients)
            for i in allergens.get(a):
                poss = poss.intersection(i)

            poss = poss-found
            if len(poss) == 1:
                word = poss.pop()
                found.add(word)
                translation[a] = word

    sorted_translations = sorted(list(translation))
    result = []
    for s in sorted_translations:
        result.append(translation.get(s))
    return ",".join(result)


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
    answer = read_file_content("inputs/ans2")

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
