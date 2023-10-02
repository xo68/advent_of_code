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


def main():
    total = 0
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

    print(f"Total:{total}")


if __name__ == "__main__":
    main()
