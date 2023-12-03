import os
import re
import sys
from collections import defaultdict


def read_inputs():
    FILE = "input.txt"
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()
    with open(FILE) as lines:
        return lines.readlines()


def main():
    res1, res2 = 0, 0

    data = read_inputs()
    special_chars = set()
    special_stars = set()
    mapping = defaultdict(list)

    # We store all non digit and "." positions
    for row in range(140):
        for col in range(140):
            # For part 1
            if data[row][col] not in "01234566789.":
                special_chars.add((row, col))
            # For part 2
            if data[row][col] in "*":
                special_stars.add((row, col))

    for row, row_data in enumerate(data):
        for value in re.finditer(r"\d+", row_data.rstrip()):
            # For each row & value,
            # calculate a coverage matrix for all positions
            coverage = set()
            for up_down in (-1, 0, 1):
                for left_right in (-1, 0, 1):
                    for v in range(value.start(0), value.end(0)):
                        coverage.add((row + up_down, v + left_right))

            # Part 1 - Sum of all numbers adjacent to a symbol
            if coverage & special_chars:
                res1 += int(value[0])

            # Part 2 - Store all values adjacent to all "*"
            for pos in coverage & special_stars:
                mapping[pos].append(int(value[0]))

    # Part 2 - Final computations
    for item in mapping.values():
        if len(item) == 2:
            res2 += item[0] * item[1]

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")


if __name__ == "__main__":
    main()
