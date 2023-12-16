import sys

sys.setrecursionlimit(10000)
grid = []
vis = set()
res = set()


def browse(r, c, d):
    # I'm out of the grid
    if c >= COL or c < 0 or r >= ROW or r < 0:
        return 0

    # I store my position (vis = visited)
    if (r, c, d) not in vis:
        vis.add((r, c, d))
        res.add((r, c))
    else:
        return 0

    # ch = current chacter in ".|/\"
    ch = grid[r][c]

    if ch == ".":
        if d == ">":
            browse(r, c + 1, d)
        if d == "<":
            browse(r, c - 1, d)
        if d == "^":
            browse(r - 1, c, d)
        if d == "v":
            browse(r + 1, c, d)
    elif ch == "\\":
        if d == ">":
            browse(r + 1, c, "v")
        if d == "<":
            browse(r - 1, c, "^")
        if d == "v":
            browse(r, c + 1, ">")
        if d == "^":
            browse(r, c - 1, "<")
    elif ch == "/":
        if d == ">":
            browse(r - 1, c, "^")
        if d == "<":
            browse(r + 1, c, "v")
        if d == "v":
            browse(r, c - 1, "<")
        if d == "^":
            browse(r, c + 1, ">")
    elif ch == "-":
        if d == ">":
            browse(r, c + 1, ">")
        if d == "<":
            browse(r, c - 1, "<")
        if d in "v^":
            browse(r, c - 1, "<")
            browse(r, c + 1, ">")
    elif ch == "|":
        if d in "><":
            browse(r - 1, c, "^")
            browse(r + 1, c, "v")
        if d == "v":
            browse(r + 1, c, "v")
        if d == "^":
            browse(r - 1, c, "^")
    else:
        return 0


if __name__ == "__main__":
    res1, res2 = 0, 0
    grid = open("input.txt").read().strip().split("\n")
    ROW = len(grid)
    COL = len(grid[0])

    # Part 1
    browse(0, 0, ">")
    res1 = len(set(res))

    # Part 2
    for c in range(COL):
        vis, res = set(), set()
        browse(0, c, "v")
        res2 = max(res2, len(set(res)))
        vis, res = set(), set()
        browse(ROW - 1, c, "^")
        res2 = max(res2, len(set(res)))

    for r in range(ROW):
        vis, res = set(), set()
        browse(r, 0, ">")
        res2 = max(res2, len(set(res)))
        vis, res = set(), set()
        browse(r, COL - 1, "<")
        res2 = max(res2, len(set(res)))

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
