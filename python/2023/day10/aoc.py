import os
import re
import sys


class Node:
    def __init__(self, c, r, l, u, d):
        self.char = c
        self.right = r
        self.left = l
        self.up = u
        self.down = d
        self.visited = False
        self.tile = False
        self.cont = False
        self.dist = 0


ROW = 140
COL = 140

map = [[None for _ in range(COL)] for _ in range(ROW)]


def part1(r, c):
    dist = 0
    next = [(r, c)]
    move = True

    while move:
        move = False
        current = next[:]
        next = []

        for pos in current:
            r = pos[0]
            c = pos[1]

            if map[r][c].right and map[r][c + 1].visited is False:
                map[r][c + 1].visited = True
                map[r][c + 1].dist = dist + 1
                next.append((r, c + 1))
                move = True
            if map[r][c].down and map[r + 1][c].visited is False:
                map[r + 1][c].visited = True
                map[r + 1][c].dist = dist + 1
                next.append((r + 1, c))
                move = True
            if map[r][c].left and map[r][c - 1].visited is False:
                map[r][c - 1].visited = True
                map[r][c - 1].dist = dist + 1
                next.append((r, c - 1))
                move = True
            if map[r][c].up and map[r - 1][c].visited is False:
                map[r - 1][c].visited = True
                map[r - 1][c].dist = dist + 1
                next.append((r - 1, c))
                move = True
        dist += 1
    return dist - 1


def check_node(ro, co):
    next = [(ro, co)]
    move = True

    if map[ro][co].visited:
        return 0

    for rr in range(0, ROW):
        for cc in range(0, COL):
            map[rr][cc].cont = False

    map[ro][co].cont = True

    while move:
        move = False
        current = next[:]
        next = []
        for pos in current:
            r = pos[0]
            c = pos[1]
            map[r][c].cont = True

            if (
                c + 1 < COL
                and map[r][c + 1].visited is not True
                and map[r][c + 1].cont is not True
            ):
                map[r][c + 1].cont = True
                next.append((r, c + 1))
                move = True
            if (
                c - 1 >= 0
                and map[r][c - 1].visited is not True
                and map[r][c - 1].cont is not True
            ):
                map[r][c - 1].cont = True
                next.append((r, c - 1))
                move = True
            if (
                r + 1 < ROW
                and map[r + 1][c].visited is not True
                and map[r + 1][c].cont is not True
            ):
                map[r + 1][c].cont = True
                next.append((r + 1, c))
                move = True
            if (
                r - 1 >= 0
                and map[r - 1][c].visited is not True
                and map[r - 1][c].cont is not True
            ):
                map[r - 1][c].cont = True
                next.append((r - 1, c))
                move = True

            if c + 1 == COL or c - 1 < 0 or r - 1 < 0 or r + 1 == ROW:
                return 0

    map[ro][co].tile = True
    return 1


def part2():
    count = 0

    for r in range(ROW):
        for c in range(COL):
            count += check_node(r, c)

    tt = ""
    for r in range(ROW):
        tt = ""
        for c in range(COL):
            if map[r][c].tile:
                tt += "O"
            elif map[r][c].visited:
                tt += "+"
            else:
                tt += "."
        print(tt)

    return count


if __name__ == "__main__":
    res1, res2 = 0, 0
    data = []
    start = (0, 0)
    lines = open("input.txt").read().split("\n")
    for i, line in enumerate(lines):
        data.append(list(line))

    for r, _ in enumerate(data):
        for c, _ in enumerate(data[r]):
            if data[r][c] == "S":
                start = (r, c)
                data[r][c] = "F"

    for r, _ in enumerate(data):
        for c, _ in enumerate(data[r]):
            rr, l, u, d = False, False, False, False
            if data[r][c] != ".":
                if r + 1 < ROW and data[r + 1][c] in "|LJ" and data[r][c] in "|7F":
                    d = True
                if r - 1 >= 0 and data[r - 1][c] in "|7F" and data[r][c] in "|LJ":
                    u = True
                if c + 1 < COL and data[r][c + 1] in "-J7" and data[r][c] in "-LF":
                    rr = True
                if c - 1 >= 0 and data[r][c - 1] in "-LF" and data[r][c] in "-J7":
                    l = True
                map[r][c] = Node(data[r][c], rr, l, u, d)
            else:
                map[r][c] = Node(".", False, False, False, False)

    res1 = part1(start[0], start[1])
    res2 = part2()

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
