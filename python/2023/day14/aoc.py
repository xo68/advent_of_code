def cycle(grid, part1=True):
    #
    # NOT SUPER CLEAN, BUT IT'S DOING THE JOB
    #

    # NORTH
    for c in range(COL):
        for r in range(ROW):
            if grid[r][c] == ".":
                for p in range(r + 1, ROW):
                    if grid[p][c] == "O":
                        grid[r][c] = "O"
                        grid[p][c] = "."
                        break
                    if grid[p][c] == "#":
                        break
    if part1:
        return grid

    # WEST
    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == ".":
                for p in range(c + 1, COL):
                    if grid[r][p] == "O":
                        grid[r][c] = "O"
                        grid[r][p] = "."
                        break
                    if grid[r][p] == "#":
                        break

    # SOUTH
    for c in range(COL):
        for r in range(ROW):
            if grid[ROW - r - 1][c] == ".":
                for p in range(r + 1, ROW):
                    if grid[ROW - p - 1][c] == "O":
                        grid[ROW - r - 1][c] = "O"
                        grid[ROW - p - 1][c] = "."
                        break
                    if grid[ROW - p - 1][c] == "#":
                        break

    # EAST
    for r in range(ROW):
        for c in range(COL):
            if grid[r][COL - c - 1] == ".":
                for p in range(c + 1, COL):
                    if grid[r][COL - p - 1] == "O":
                        grid[r][COL - c - 1] = "O"
                        grid[r][COL - p - 1] = "."
                        break
                    if grid[r][COL - p - 1] == "#":
                        break
    return grid


def results(grid):
    res = 0
    for r, row in enumerate(grid):
        res += row.count("O") * (ROW - r)
    return res


if __name__ == "__main__":
    res1, res2 = 0, 0
    lines = open("input.txt").read().splitlines()
    data = []
    for l in lines:
        data.append(list(l))
    data2 = data[:]

    ROW = len(data)
    COL = len(data[0])

    # PART 1
    data = cycle(data)
    res1 = results(data)

    # PART 2
    already_seen = [tuple(tuple(row) for row in data2)]
    iter, found = 0, 0
    while iter < 1000000000:
        iter += 1
        data2 = cycle(data2, part1=False)

        tmp = tuple(tuple(row) for row in data2)
        if tmp in already_seen:
            found = already_seen.index(tmp)
            break
        else:
            already_seen.append(tmp)

    position = (1000000000 - found) % (iter - found) + found
    res2 = results(already_seen[position])

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
