import os
import sys

FILE = "input.txt"
VALUES = {}


# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# ASCII -> A = 65; Z = 90 & a = 97; z = 122
def init_values():
    val = 1
    for x in range(97, 123):
        VALUES[chr(x)] = val
        val = val + 1
    for x in range(65, 91):
        VALUES[chr(x)] = val
        val = val + 1


# Function for part2 (badges)
def check_badges(l: list) -> int:
    i0, i1, i2 = l[0], l[1], l[2]
    for c0 in i0[:-1]:
        for c1 in i1[:-1]:
            for c2 in i2[:-1]:
                if c0 == c1 == c2:
                    return VALUES[c0]
    return 0


def main():
    # Part 1
    total = 0
    total_part2 = 0
    first_part = ""
    second_part = ""
    size = 0
    init_values()

    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()

    with open(FILE) as f:
        lines = f.readlines()

    for line in lines:
        found_char = ""
        size = len(line)
        first_part = line[: size // 2]
        second_part = line[size // 2 : -1]

        for c1 in first_part:
            for c2 in second_part:
                if c1 == c2:
                    found_char = c1

        total = total + VALUES[found_char]
        # print(f"Char:{found_char}, Val{VALUES[found_char]}")

    print(f"Total_part1:{total}")

    # PART 2 of the exercice (Badges)
    badges = []
    x = 0
    for line in lines:
        badges.insert(x, line)
        x = x + 1
        if x // 3:
            total_part2 = total_part2 + check_badges(badges)
            x = 0

    print(f"Total_part2:{total_part2}")


if __name__ == "__main__":
    main()
