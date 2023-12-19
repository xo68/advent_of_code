import re


# Get the distinct elements for [xmas][<>]VALUE:[name]
def get_elements(e):
    name, comp = e[0], e[1]
    value, target = e[2:].split(":")
    return (name, comp, int(value), target)


def run_part2(pos, name):
    if name == "R":
        return 0
    elif name == "A":
        p = 1
        for l, h in pos.values():
            p *= h - l + 1
        return p

    r, f = wf[name]

    total = 0
    for val in r:
        k, c, n, t = get_elements(val)
        l, h = pos[k]
        if c == "<":
            ins = (l, n - 1)
            out = (n, h)
        else:
            ins = (n + 1, h)
            out = (l, n)

        if ins[0] <= ins[1]:
            pos1 = dict(pos)
            pos1[k] = ins
            total += run_part2(pos1, t)

        if out[0] <= out[1]:
            pos = dict(pos)
            pos[k] = out
        else:
            break
    else:
        total += run_part2(pos, f)

    return total


if __name__ == "__main__":
    res1, res2 = 0, 0
    part1, part2 = open("input.txt").read().split("\n\n")

    # Read the workflows
    wf = {}
    for row in part1.splitlines():
        name, row = row.split("{")
        *tmp, end = row.split(",")
        wf[name] = (tmp, end[:-1])

    # Read the ratings
    ratings = []
    for row in part2[:-1].splitlines():
        x, m, a, s = re.findall("[0-9]+", row)
        ratings.append({"x": int(x), "m": int(m), "a": int(a), "s": int(s)})

    # Part 1
    for r in ratings:
        current = wf["in"]
        res = 0
        found = False
        while not found:
            for val in current[0]:
                n, c, v, t = get_elements(val)
                if eval(f"{r[n]} {c} {v}"):
                    if t not in "AR":
                        current = wf[t]
                    else:
                        found = True
                        res = t
                    break
            else:
                if current[1] not in "AR":
                    current = wf[current[1]]
                else:
                    found = True
                    res = current[1]

        if res == "A":
            res1 += r["x"] + r["m"] + r["a"] + r["s"]

    # Part 2
    pos = {}
    for i in "xmas":
        pos[i] = (1, 4000)
    res2 = run_part2(pos, "in")

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
