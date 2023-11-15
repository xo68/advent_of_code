import os
import re
import sys

FILE = "input.txt"

# https://adventofcode.com/2022/day/10


def read_inputs() -> list:
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()
    with open(FILE) as lines:
        return lines.readlines()


def part2():
    input = read_inputs()
    addx = re.compile(r"(^addx )(.*)")
    CRT = [["#" for _ in range(6)] for _ in range(40)]
    x, y, cycles = 0, 0, 0
    spos = 1

    for line in input:
        if addx.match(line):
            cycles += 1
            if x == spos or x == spos - 1 or x == spos + 1:
                CRT[x][y] = "#"
            else:
                CRT[x][y] = " "

            x += 1
            if cycles % 40 == 0:
                x = 0
                y += 1

            cycles += 1
            if x == spos or x == spos - 1 or x == spos + 1:
                CRT[x][y] = "#"
            else:
                CRT[x][y] = " "
            spos += int(addx.match(line).group(2))
        else:
            cycles += 1
            if x == spos or x == spos - 1 or x == spos + 1:
                CRT[x][y] = "#"
            else:
                CRT[x][y] = " "

        x += 1
        if cycles % 40 == 0:
            x = 0
            y += 1

    print("Part2")
    for i in range(6):
        row = ""
        for j in range(40):
            row += str(CRT[j][i])
        print(row)


def part1():
    input = read_inputs()
    addx = re.compile(r"(^addx )(.*)")
    inc = 20
    cycles = 0
    signal = 0
    X = 1

    for line in input:
        cycles += 1
        if cycles == inc:
            inc += 40
            signal += cycles * X
        if addx.match(line):
            cycles += 1
            if cycles == inc:
                inc += 40
                signal += cycles * X
            X += int(addx.match(line).group(2))

    print(f"part1: {signal} ")


if __name__ == "__main__":
    part1()
    part2()
