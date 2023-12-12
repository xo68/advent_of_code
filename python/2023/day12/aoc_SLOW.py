#####################################
# THIS IS CRAP - BRUTE FORCE PART 1 #
#####################################


def get_posibilities(val, idx, opt):
    if opt is None:
        tmp = []
        if val[0] in ".#":
            tmp.append(val[0] + val[1:])
        else:
            tmp.append("." + val[1:])
            tmp.append("#" + val[1:])
    else:
        tmp = opt[:]
        if val[idx] == "?":
            for o in opt:
                tmp.append(o[0:idx] + "." + o[idx + 1 :])
                tmp.append(o[0:idx] + "#" + o[idx + 1 :])

    if idx < len(val) - 1 and "?" in val[idx:]:
        return get_posibilities(val, idx + 1, tmp)
    else:
        return tmp


def process(left, right):
    count = 0

    all_pos = get_posibilities(left, 0, None)
    r = list(map(int, right.split(",")))

    for p in all_pos:
        found = True
        s = p.split(".")
        s = [x for x in s if x != ""]
        if len(s) == len(r):
            for i, c in enumerate(s):
                if c != r[i] * "#":
                    found = False
        else:
            found = False

        if found:
            count += 1
    return count


if __name__ == "__main__":
    res1 = 0
    lines = open("input.txt").read().split("\n")
    for i, line in enumerate(lines[:-1]):
        left, right = line.split()
        res1 += process(left, right)
    print(f"Result1:{res1}")
