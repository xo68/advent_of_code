grid = []
path = []

LEFT = "-LF"
RIGHT = "-J7"
UP = "|7F"
DOWN = "|LJ"


# Get starting point
def get_start():
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if grid[r][c] == "S":
                return r, c


# Find CHAR replacement for S based on neighboors
def replace_S(r, c):
    if grid[r][c - 1] in LEFT and grid[r][c + 1] in RIGHT:
        return "-"
    if grid[r - 1][c] in UP and grid[r + 1][c] in DOWN:
        return "|"
    if grid[r - 1][c] in UP and grid[r][c + 1] in RIGHT:
        return "L"
    if grid[r][c - 1] in LEFT and grid[r - 1][c] in UP:
        return "J"
    if grid[r][c - 1] in LEFT and grid[r + 1][c] in DOWN:
        return "7"
    if grid[r][c + 1] in RIGHT and grid[r + 1][c] in DOWN:
        return "F"


if __name__ == "__main__":
    res1, res2 = 0, 0
    lines = open("input.txt").read().split()
    for line in lines:
        grid.append(list(line))
    ROW = len(grid)
    COL = len(grid[0])

    # Get starting point
    R, C = get_start()
    grid[R][C] = replace_S(R, C)

    # Part 1
    path.append((R, C))
    r, c = (0, 0)
    end = False
    while not end:
        r, c = path[-1]
        g = grid[r][c]

        if (
            c + 1 < COL
            and g in LEFT
            and grid[r][c + 1] in RIGHT
            and (r, c + 1) not in path
        ):
            path.append((r, c + 1))
        elif (
            c - 1 >= 0
            and g in RIGHT
            and grid[r][c - 1] in LEFT
            and (r, c - 1) not in path
        ):
            path.append((r, c - 1))
        elif (
            r + 1 < ROW
            and g in UP
            and grid[r + 1][c] in DOWN
            and (r + 1, c) not in path
        ):
            path.append((r + 1, c))
        elif (
            r - 1 >= 0 and g in DOWN and grid[r - 1][c] in UP and (r - 1, c) not in path
        ):
            path.append((r - 1, c))
        else:
            end = True
    res1 = len(path) // 2

    # Part 2 --> SHOELACE + PICK'S THEOREM
    tmp = 0
    for i in range(len(path)):
        tmp += path[i][0] * path[i - 1][1] - path[i - 1][0] * path[i][1]
    SHOELACE = abs(tmp) // 2
    res2 = SHOELACE - len(path) // 2 + 1

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
