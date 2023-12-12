cache = {}


def process(l, r):
    res = 0
    if l == "":
        return 1 if r == () else 0

    if r == ():
        return 0 if "#" in l else 1

    k = (l, r)

    if k in cache:
        return cache[k]

    if l[0] in ".?":
        res += process(l[1:], r)

    if l[0] in "#?":
        if (
            r[0] <= len(l)
            and "." not in l[: r[0]]
            and (r[0] == len(l) or l[r[0]] != "#")
        ):
            res += process(l[r[0] + 1 :], r[1:])
    cache[k] = res
    return res


if __name__ == "__main__":
    res1, res2 = 0, 0
    lines = open("input.txt")
    for line in lines:
        l, r = line.split()
        r = tuple(map(int, r.split(",")))

        # Part 1
        res1 += process(l, r)

        # Part 2
        l = "?".join([l] * 5)
        r = r * 5
        res2 += process(l, r)

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
