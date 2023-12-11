if __name__ == "__main__":
    res1, res2 = 0, 0

    data = []
    lines = open("input.txt").read().split()
    for line in lines:
        data.append(list(line))

    # Find all empty COL and ROW & Add all Positions in p
    row = set()
    col = set()
    p = []
    for r, _ in enumerate(data):
        if data[r].count("#") == 0:
            row.add(r)
        for c, _ in enumerate(data[r]):
            if data[r][c] == "#":
                col.add(c)
                p.append((r, c))
    col = {i for i in range(len(data[0]))} - col

    # Find all PAIRs
    pairs = []
    x = 0
    for p1 in range(len(p)):
        for p2 in range(1 + x, len(p)):
            pairs.append((p[p1], p[p2]))
        x = x + 1

    # Compute Part 1 & 2
    for p in pairs:
        start, end = p[0], p[1]
        empty_r, empty_c = 0, 0
        for r in row:
            if start[0] < r < end[0]:
                empty_r += 1
        for c in col:
            if min(start[1], end[1]) < c < max(start[1], end[1]):
                empty_c += 1
        r = abs(start[0] - end[0])
        c = abs(start[1] - end[1])
        res1 += r + empty_r + c + empty_c
        res2 += r + empty_r * int(1e6 - 1) + c + empty_c * int(1e6 - 1)

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
