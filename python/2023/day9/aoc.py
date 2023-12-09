def process_input(line, part):
    tmp = []
    res = [line[:]]
    while True:
        for i in range(0, len(res[-1]) - 1):
            tmp.append(res[-1][i + 1] - res[-1][i])
        res.append(tmp)
        if len(set(tmp)) == 1:
            res.append([0 for _ in range(len(res[-1]) - 1)])
            break
        tmp = []

    for line in res:
        line.append(0)
        line.insert(0, 0)

    if part == 1:
        for i in range(1, len(res)):
            res[-i - 1][-1] = res[-i][-1] + res[-i - 1][-2]
        return res[0][-1]

    if part == 2:
        for i in range(1, len(res)):
            res[-i - 1][0] = res[-i - 1][1] - res[-i][0]
        return res[0][0]


if __name__ == "__main__":
    res1, res2 = 0, 0
    lines = open("input.txt").read().split("\n")

    for line in lines[:-1]:
        row = list(map(int, line.split(" ")))
        res1 += process_input(row, part=1)
        res2 += process_input(row, part=2)

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
