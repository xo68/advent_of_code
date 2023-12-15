def hash(st):
    v = 0
    for c in st:
        v = (v + ord(c)) * 17 % 256
    return v


if __name__ == "__main__":
    res1, res2 = 0, 0
    boxes = [[] for _ in range(256)]
    lines = open("input.txt").read().strip().split(",")

    for line in lines:
        # Part1
        v = hash(line)
        res1 += v

        # Part2
        if line[-1] == "-":
            l = line[0:-1]
            target = hash(l)
            for i in range(len(boxes[target])):
                if boxes[target][i][0:-2] == l:
                    boxes[target].pop(i)
                    break
        else:
            repl = False
            l = line[0:-2]
            target = hash(l)
            for i in range(len(boxes[target])):
                if boxes[target][i][:-2] == l:
                    boxes[target][i] = l + " " + line[-1]
                    repl = True
                    break
            if not repl:
                boxes[target].append(l + " " + line[-1])

    for b, box in enumerate(boxes):
        for v, val in enumerate(box):
            res2 += (b + 1) * (v + 1) * int(val[-1])

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
