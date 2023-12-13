def process(data, part2=False):
    for i in range(1, len(data)):
        up = data[:i][::-1]
        down = data[i:]

        if part2:
            diff = 0
            for x, y in zip(up, down):
                for x1, y1 in zip(x, y):
                    if x1 != y1:
                        diff += 1
            if diff == 1:
                return i
        else:
            s = min(len(down), len(up))
            if up[:s] == down[:s]:
                return i
    return 0


if __name__ == "__main__":
    res1, res2 = 0, 0
    lines = open("input.txt").read().split("\n")
    data = []
    while lines:
        if lines and lines[0] != "":
            data.append(lines.pop(0))
        else:
            data_r = list(zip(*data))
            res1 += process(data) * 100
            res1 += process(data_r)
            res2 += process(data, part2=True) * 100
            res2 += process(data_r, part2=True)
            data = []
            lines.pop(0)

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
