POSITIONS = {
    "0": (0, 1),
    "R": (0, 1),
    "1": (1, 0),
    "D": (1, 0),
    "2": (0, -1),
    "L": (0, -1),
    "3": (-1, 0),
    "U": (-1, 0),
}

if __name__ == "__main__":
    res1, res2 = 0, 0
    data1, data2 = [], []

    lines = open("input.txt").read().strip().split("\n")

    for line in lines:
        dir, val, code = line.split(" ")
        data1.append((dir, int(val)))
        data2.append(((code[-2]), int(code[-7:-2], 16)))

    for p in (1, 2):
        bound = 0
        grid = [(0, 0)]

        data = data1 if p == 1 else data2

        for d, v in data:
            bound += v  # Count all boundaries
            dir_r, dir_c = POSITIONS[d]
            last_r, last_c = grid[-1]
            grid.append((last_r + dir_r * v, last_c + dir_c * v))

        # Shoelace formula
        SF = 0
        for i in range(1, len(grid) - 1):
            SF += grid[i][0] * (grid[i - 1][1] - grid[i + 1][1])
        SF = abs(SF // 2)

        # Pick formula: Area = interior_points + boundaries // 2 - 1
        # Area = Shoelace formula
        PF = SF - bound // 2 + 1

        if p == 1:
            res1 = PF + bound
        else:
            res2 = PF + bound

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
