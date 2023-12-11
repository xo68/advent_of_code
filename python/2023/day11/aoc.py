if __name__ == "__main__":
    res1, res2 = 0, 0

    data = open("input.txt").read().split()

    row = [r for r, row in enumerate(data) if all(c == "." for c in row)]
    col = [c for c, col in enumerate(zip(*data)) if all(c == "." for c in col)]
    p = [
        (r, c)
        for r, row in enumerate(data)
        for c, col in enumerate(row)
        if data[r][c] == "#"
    ]

    pairs = [(p[p1], p[p2]) for p1 in range(len(p)) for p2 in range(p1 + 1, len(p))]

    for p in pairs:
        empty_r, empty_c = 0, 0
        for r in row:
            if p[0][0] < r < p[1][0]:
                empty_r += 1
        for c in col:
            if min(p[0][1], p[1][1]) < c < max(p[0][1], p[1][1]):
                empty_c += 1
        res1 += abs(p[0][0] - p[1][0]) + empty_r + abs(p[0][1] - p[1][1]) + empty_c
        res2 += (
            abs(p[0][0] - p[1][0])
            + empty_r * int(1e6 - 1)
            + abs(p[0][1] - p[1][1])
            + empty_c * int(1e6 - 1)
        )

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
