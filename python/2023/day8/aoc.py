from math import lcm

if __name__ == "__main__":
    res1, res2 = 0, 0
    paths = {}

    lines = open("input.txt").read().split("\n")
    dir = list(lines[0])
    for line in lines[2:-1]:
        paths[line[0:3]] = (line[7:10], line[12:15])

    # Part 1
    cur = "AAA"
    while cur != "ZZZ":
        if dir[res1 % len(dir)] == "L":
            cur = paths.get(cur)[0]
        else:
            cur = paths.get(cur)[1]
        res1 += 1

    # Part 2
    start = [s for s in paths.keys() if s[-1] == "A"]
    end = []
    for s in start:
        cur = s
        i = 0
        while cur[-1] != "Z":
            if dir[i % len(dir)] == "L":
                cur = paths.get(cur)[0]
            else:
                cur = paths.get(cur)[1]
            i += 1
        end.append(i)
    res2 = lcm(*end)

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
