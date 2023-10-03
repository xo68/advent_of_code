import os
import sys

FILE = "input.txt"


def main():
    cal_current = 0
    cal_table = []
    top_elves = 0

    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()

    with open(FILE) as f:
        lines = f.readlines()

    for line in lines:
        if line == "\n":
            cal_table.append(cal_current)
            cal_current = 0
        else:
            cal_current = cal_current + int(line)

    cal_table.sort()

    # Elf having the most calories
    top_elves = cal_table.pop()
    print(f"Top 1 elf -> {top_elves}")

    # Add the next 2 elves
    top_elves = top_elves + cal_table.pop()
    top_elves = top_elves + cal_table.pop()
    print(f"Top 3 elves -> {top_elves}")


if __name__ == "__main__":
    main()
