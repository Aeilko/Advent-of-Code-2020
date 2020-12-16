from utils.file import read_file_content


def solve_part1(inp: str) -> int:
    inp = inp[:-1].split("\n\n")

    # Parse restrictions
    inp_fields = inp[0].split("\n")
    fields = {}
    for line in inp_fields:
        (name, val) = line.split(": ")
        vals = [item.split("-") for item in val.split(" or ")]
        vals = [[int(x) for x in sublist] for sublist in vals]
        name = name.replace(" ", "_")
        fields[name] = vals

    # Check tickets
    inp_tickets = inp[2].split("\n")
    inp_tickets.pop(0)
    r = 0
    for line in inp_tickets:
        vals = [int(x) for x in line.split(",")]
        for v in vals:
            valid = False
            for f in fields:
                field = fields.get(f)
                if field[0][0] <= v <= field[0][1] or field[1][0] <= v <= field[1][1]:
                    valid = True
                    break
            if not valid:
                r += v
    return r


def solve_part2(inp: str) -> int:
    inp = inp[:-1].split("\n\n")

    # Parse restrictions
    inp_fields = inp[0].split("\n")
    fields = {}
    for line in inp_fields:
        (name, val) = line.split(": ")
        vals = [item.split("-") for item in val.split(" or ")]
        vals = [[int(x) for x in sublist] for sublist in vals]
        name = name.replace(" ", "_")
        fields[name] = vals

    # Check valid tickets
    inp_tickets = inp[2].split("\n")
    inp_tickets.pop(0)
    tickets = []
    for line in inp_tickets:
        vals = [int(x) for x in line.split(",")]
        for v in vals:
            valid = False
            for f in fields:
                field = fields.get(f)
                if field[0][0] <= int(v) <= field[0][1] or field[1][0] <= int(v) <= field[1][1]:
                    valid = True
                    break
            if not valid:
                break
        if valid:
            tickets.append(vals)

    # Determine fields
    fields_possible = []
    all_fields = []
    for x in fields:
        all_fields.append(x)
    for i in range(len(tickets[0])):
        fields_possible.append(all_fields.copy())

    for ticket in tickets:
        for i in range(len(ticket)):
            val = ticket[i]
            for f in fields_possible[i]:
                field = fields.get(f)
                if (val < field[0][0] or val > field[0][1]) and (val < field[1][0] or val > field[1][1]):
                    fields_possible[i].remove(f)

    # Check which fields have been found, remove them from the other fields.
    confirmed_fields = []
    # 40 was randomly chosen, to do this properly we should check if confirmed_fields and fields_possible have
    # changed during a cycle
    for zz in range(40):
        for i in range(len(fields_possible)):
            if len(fields_possible[i]) == 1:
                if fields_possible[i][0] not in confirmed_fields:
                    confirmed_fields.append(fields_possible[i][0])
            else:
                fields_possible[i] = list(set(fields_possible[i])-set(confirmed_fields))

    # Calculate result
    my_ticket = [int(x) for x in inp[1].split("\n")[1].split(",")]
    r = 1
    for i in range(len(my_ticket)):
        x = fields_possible[i][0]
        if len(x) > 9 and x[:9] == "departure":
            r *= my_ticket[i]
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
