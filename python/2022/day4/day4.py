import os
import sys

FILE = "input.txt"
VALUES = {}


def main():
    total = 0
    total2 = 0

    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()

    with open(FILE) as f:
        lines = f.readlines()

    for l in lines:
        line = l.replace("\n", "")
        spaces = line.split(",")

        elf1 = spaces[0].split("-")
        elf2 = spaces[1].split("-")

        # Results for part 1 - Full overlap
        # Results for part 2 - Any partial overlap
        if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
            total = total + 1
            total2 = total2 + 1
        elif int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
            total = total + 1
            total2 = total2 + 1
        elif int(elf2[0]) >= int(elf1[0]) and int(elf2[0]) <= int(elf1[1]):
            total2 = total2 + 1
        elif int(elf2[1]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1]):
            total2 = total2 + 1

    print(f"Total Part1:{total}")
    print(f"Total Part2:{total2}")


if __name__ == "__main__":
    main()
