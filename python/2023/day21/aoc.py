def find_start(grid, ROW, COL):
    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == "S":
                grid[r][c] = "."
                return (r, c)


def compute(r, c, s):
    next = [(r, c)]
    for s in range(0, s):
        current = next[:]
        next = []
        while current:
            r, c = current.pop()
            if c + 1 < COL and grid[r][c + 1] == ".":
                if (r, c + 1) not in next:
                    next.append((r, c + 1))
            if c - 1 >= 0 and grid[r][c - 1] == ".":
                if (r, c - 1) not in next:
                    next.append((r, c - 1))
            if r - 1 >= 0 and grid[r - 1][c] == ".":
                if (r - 1, c) not in next:
                    next.append((r - 1, c))
            if r + 1 < ROW and grid[r + 1][c] == ".":
                if (r + 1, c) not in next:
                    next.append((r + 1, c))
    return len(next)


if __name__ == "__main__":
    grid = []
    lines = open("input.txt").read().strip().split("\n")
    for line in lines:
        grid.append(list(line))

    ROW = len(grid)
    COL = len(grid[0])
    SIZE = ROW
    R, C = find_start(grid, ROW, COL)

    # Part 1
    STEPS = 64
    res1 = compute(R, C, STEPS)

    # Part 2
    STEPS = 26501365
    map_w = STEPS // SIZE - 1

    odd = (map_w // 2 * 2 + 1) ** 2
    even = ((map_w + 1) // 2 * 2) ** 2

    odd_p = compute(R, C, COL * 2 + 1)
    even_p = compute(R, C, COL * 2)

    corner_t = compute(ROW - 1, C, SIZE - 1)
    corner_r = compute(R, 0, SIZE - 1)
    corner_b = compute(0, C, SIZE - 1)
    corner_l = compute(R, COL - 1, SIZE - 1)

    small_tr = compute(ROW - 1, 0, SIZE // 2 - 1)
    small_tl = compute(ROW - 1, COL - 1, SIZE // 2 - 1)
    small_br = compute(0, 0, SIZE // 2 - 1)
    small_bl = compute(0, COL - 1, SIZE // 2 - 1)

    large_tr = compute(ROW - 1, 0, SIZE * 3 // 2 - 1)
    large_tl = compute(ROW - 1, COL - 1, SIZE * 3 // 2 - 1)
    large_br = compute(0, 0, SIZE * 3 // 2 - 1)
    large_bl = compute(0, COL - 1, SIZE * 3 // 2 - 1)

    res2 = (
        odd * odd_p
        + even * even_p
        + corner_t
        + corner_r
        + corner_b
        + corner_l
        + (map_w + 1) * (small_tr + small_tl + small_br + small_bl)
        + map_w * (large_tr + large_tl + large_br + large_bl)
    )

    print(f"Result1:{res1}")  # 3'847
    print(f"Result2:{res2}")  # 637'537'341'306'357
