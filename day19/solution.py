import re


from utils.file import read_file_content


def get_regex(rule_id: int, regex_rules: dict, og_rules: dict) -> str:
    inp = og_rules[rule_id]
    if inp in ['"a"', '"b"']:
        regex_rules[rule_id] = str(inp[1])
        return inp
    else:
        rules = []
        inp = inp.split(" | ")
        for ors in inp:
            rule = ""
            parts = ors.split(" ")
            for part in parts:
                part = int(part)
                if part not in regex_rules:
                    get_regex(part, regex_rules, og_rules)
                rule += regex_rules.get(part)
            rules.append("(" + rule + ")")

        if len(rules) == 1:
            r = rules[0]
        else:
            r = "(" + "|".join(rules) + ")"

        regex_rules[rule_id] = r
        return r


def solve_part1(inp: str) -> int:
    (rules, inp) = inp[:-1].split("\n\n")
    rules = rules.split("\n")
    og_rules = [None]*len(rules)
    for line in rules:
        (id, rule) = line.split(": ")
        og_rules[int(id)] = rule

    regex = get_regex(0, {}, og_rules)

    r = 0
    inp = inp.split("\n")
    for line in inp:
        if re.match("^" + regex + "$", line):
            r += 1

    return r


def get_regex_2(rule_id: int, regex_rules: dict, og_rules: dict) -> str:
    inp = og_rules[rule_id]
    if inp in ['"a"', '"b"']:
        regex_rules[rule_id] = str(inp[1])
        return inp
    elif rule_id in [8, 11]:
        rule_42 = get_regex_2(42, regex_rules, og_rules)
        rule_31 = get_regex_2(31, regex_rules, og_rules)
        if rule_id == 8:
            r = "(" + rule_42 + "+" + ")"
        else:
            # Best solution for recursive regular expression
            rules = []
            for i in range(1, 10):
                rule = "(" + rule_42 + "{" + str(i) + "}" + rule_31 + "{" + str(i) + "}" + ")"
                rules.append(rule)
            r = "(" + "|".join(rules) + ")"
        regex_rules[rule_id] = r
        return r
    else:
        rules = []
        inp = inp.split(" | ")
        for ors in inp:
            rule = ""
            parts = ors.split(" ")
            for part in parts:
                part = int(part)
                if part not in regex_rules:
                    get_regex_2(part, regex_rules, og_rules)
                rule += regex_rules.get(part)
            rules.append("(" + rule + ")")

        if len(rules) == 1:
            r = rules[0]
        else:
            r = "(" + "|".join(rules) + ")"

        regex_rules[rule_id] = r
        return r


def solve_part2(inp: str) -> int:
    (rules, inp) = inp[:-1].split("\n\n")
    rules = rules.split("\n")
    og_rules = [None] * len(rules)
    for line in rules:
        (id, rule) = line.split(": ")
        og_rules[int(id)] = rule

    regex = get_regex_2(0, {}, og_rules)

    r = 0
    inp = inp.split("\n")
    for line in inp:
        if re.match("^" + regex + "$", line):
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
