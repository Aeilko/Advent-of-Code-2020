import re

from utils.file import read_file_content


def solve_part1(inp: str) -> int:
    inp = [x.split("\n") for x in inp[:-1].split("\n\n")]
    deck1 = [int(x) for x in inp[0][1:]]
    deck2 = [int(x) for x in inp[1][1:]]
    while len(deck1) > 0 and len(deck2) > 0:
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)

    if len(deck1) > 0:
        winning_deck = deck1
    else:
        winning_deck = deck2

    r = 0
    for i in range(len(winning_deck)):
        r += winning_deck[i]*(len(winning_deck)-i)
    return r


def recursive_combat(deck1: list, deck2: list) -> (bool, list):
    prev_decks1 = []
    prev_decks2 = []
    while len(deck1) > 0 and len(deck2) > 0:
        if deck1 in prev_decks1 or deck2 in prev_decks2:
            return (True, deck1)
        else:
            prev_decks1.append(list(deck1))
            prev_decks2.append(list(deck2))

            c1 = deck1.pop(0)
            c2 = deck2.pop(0)

            if len(deck1) >= c1 and len(deck2) >= c2:
                (p1_win, winning_deck) = recursive_combat(deck1[:c1], deck2[:c2])
            else:
                p1_win = c1 > c2

            if p1_win:
                deck1.append(c1)
                deck1.append(c2)
            else:
                deck2.append(c2)
                deck2.append(c1)

    p1_win = False
    w_deck = deck2
    if len(deck1) > 0:
        p1_win = True
        w_deck = deck1
    return (p1_win, w_deck)


def solve_part2(inp: str) -> int:
    inp = [x.split("\n") for x in inp[:-1].split("\n\n")]
    deck1 = [int(x) for x in inp[0][1:]]
    deck2 = [int(x) for x in inp[1][1:]]

    (player1_win, winning_deck) = recursive_combat(deck1, deck2)

    r = 0
    for i in range(len(winning_deck)):
        r += winning_deck[i] * (len(winning_deck) - i)
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
