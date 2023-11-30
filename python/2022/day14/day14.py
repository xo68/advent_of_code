import os
import re
import sys

FILE = "input.txt"


def read_inputs() -> list:
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()
    with open(FILE) as lines:
        return lines.readlines()


def print_map(map):
    print("-----------MAP----------")
    for i in range(len(map)):
        row = str() + str(i)
        for j in range(450, 600):
            row = row + map[i][j]
        print(row)


def process():
    result = 0
    map = [["." for _ in range(1000)] for _ in range(170)]
    # [row][column]

    # BUILD THE MAP
    for line in read_inputs():
        items = line.rstrip().split(" -> ")

        item = items.pop(0)
        x, y = item.split(",")
        x = int(x)
        y = int(y)
        while items:
            item = items.pop(0)
            x1, y1 = item.split(",")
            x1 = int(x1)
            y1 = int(y1)

            if x == x1:
                if y >= y1:
                    for yy in range(y1, y + 1):
                        map[yy][x] = "#"
                else:
                    for yy in range(y, y1 + 1):
                        map[yy][x] = "#"

            if y == y1:
                if x > x1:
                    for xx in range(x1, x + 1):
                        map[y][xx] = "#"
                else:
                    for xx in range(x, x1 + 1):
                        map[y][xx] = "#"

            x = x1
            y = y1

    # SAND IS FALLING
    next = True
    while next:
        result += 1

        # Part 1
        # nrow, ncol = check_move1(map, 1, 500)  # We start at 1,500

        # Part 2 -> Add  to input file the floor : 0,163 -> 999,163
        nrow, ncol = check_move2(map, 0, 500)  # We start at 1,500

        map[nrow][ncol] = "o"

        if nrow == -1:
            next = False
    print_map(map)
    print(f"Result: {result-1}")


# Part1 - A BIT OF RECURSIVITY :)
def check_move1(map, row, col):
    if map[row][col] == ".":
        row += 1
    else:
        if map[row][col - 1] == ".":
            col -= 1
        elif map[row][col + 1] == ".":
            col += 1
        else:
            return row - 1, col
    if row == 163:  # Falling in void
        return -1, -1
    return check_move1(map, row, col)


# Part2 - A BIT OF RECURSIVITY :)
def check_move2(map, row, col):
    if map[row][col] == ".":
        row += 1
    else:
        if map[row][col - 1] == ".":
            col -= 1
        elif map[row][col + 1] == ".":
            col += 1
        else:
            return row - 1, col
    if row == 0:  # Top is reached
        return -1, -1
    return check_move2(map, row, col)


if __name__ == "__main__":
    process()
