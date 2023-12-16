import sys

sys.setrecursionlimit(10000)
grid = []
vis = set()

#
# NOT VERY CLEAN, REFACTORING IN PROGRESS
#


def display():
    for r in grid:
        print(r)


def browse(r, c, d):
    if c >= COL or c < 0:
        return 0
    if r >= ROW or r < 0:
        return 0

    if (r, c, d) in vis:
        return 0
    else:
        vis.add((r, c, d))

    ch = grid[r][c]

    # Handle "."
    if ch == ".":
        if d == ">":
            browse(r, c + 1, d)
        if d == "<":
            browse(r, c - 1, d)
        if d == "^":
            browse(r - 1, c, d)
        if d == "v":
            browse(r + 1, c, d)

    # Handle "\"
    if ch == "\\" and d == ">":
        browse(r + 1, c, "v")
    if ch == "\\" and d == "<":
        browse(r - 1, c, "^")
    if ch == "\\" and d == "v":
        browse(r, c + 1, ">")
    if ch == "\\" and d == "^":
        browse(r, c - 1, "<")

    # Handle "/"
    if ch == "/" and d == ">":
        browse(r - 1, c, "^")
    if ch == "/" and d == "<":
        browse(r + 1, c, "v")
    if ch == "/" and d == "v":
        browse(r, c - 1, "<")
    if ch == "/" and d == "^":
        browse(r, c + 1, ">")

    # Handle "-"
    if ch == "-" and d == ">":
        browse(r, c + 1, ">")
    if ch == "-" and d == "<":
        browse(r, c - 1, "<")
    if ch == "-" and d in "v^":
        browse(r, c - 1, "<")
        browse(r, c + 1, ">")

    # Handle "|"
    if ch == "|" and d in "><":
        browse(r - 1, c, "^")
        browse(r + 1, c, "v")
    if ch == "|" and d == "v":
        browse(r + 1, c, "v")
    if ch == "|" and d == "^":
        browse(r - 1, c, "^")


if __name__ == "__main__":
    res1, res2 = 0, 0
    grid = open("input.txt").read().strip().split("\n")
    ROW = len(grid)
    COL = len(grid[0])
    browse(0, 0, ">")

    r = set()
    for i in vis:
        r.add((i[0], i[1]))
    res1 = len(set(r))

    for c in range(COL):
        vis = set()
        browse(0, c, "v")

        r = set()
        for i in vis:
            r.add((i[0], i[1]))
        res2 = max(res2, len(set(r)))

    for c in range(COL):
        vis = set()
        browse(ROW - 1, c, "^")

        r = set()
        for i in vis:
            r.add((i[0], i[1]))
        res2 = max(res2, len(set(r)))

    for r in range(ROW):
        vis = set()
        browse(r, 0, ">")

        r = set()
        for i in vis:
            r.add((i[0], i[1]))
        res2 = max(res2, len(set(r)))

    for r in range(ROW):
        vis = set()
        browse(r, COL - 1, "<")

        r = set()
        for i in vis:
            r.add((i[0], i[1]))
        res2 = max(res2, len(set(r)))

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
