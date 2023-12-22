import re

# brick = [x, y, z, x1,y1,z1]
#          0  1  2  3  4  5


# 2 bricks will intersect ?
def intersect(b1, b2):
    if max(b1[0], b2[0]) <= min(b1[3], b2[3]):
        if max(b1[1], b2[1]) <= min(b1[4], b2[4]):
            return True
    return False


if __name__ == "__main__":
    res1, res2 = 0, 0
    bricks = []

    # Read & Prepare data
    lines = open("input.txt").read().strip().split("\n")
    for line in lines:
        x, y, z, x1, y1, z1 = re.findall("\d+", line)
        bricks.append([int(x), int(y), int(z), int(x1), int(y1), int(z1)])
    bricks.sort(key=lambda b: b[2])

    # Bricks are falling
    for idx, b in enumerate(bricks):
        z = 1
        for chk in bricks[:idx]:
            if intersect(b, chk):
                z = max(z, chk[5] + 1)
            b[5] = b[5] - b[2] + z
            b[2] = z

    # Check who is supporting who...
    support_bricks = {}
    support = {}
    for i in range(len(bricks)):
        support_bricks[i] = set()
        support[i] = set()

    for j, up in enumerate(bricks):
        for i, lo in enumerate(bricks[:j]):
            if intersect(lo, up) and up[2] == lo[5] + 1:
                support_bricks[i].add(j)
                support[j].add(i)

    for i in range(len(bricks)):
        # Part1
        for j in support_bricks[i]:
            if not len(support[j]) >= 2:
                break
        else:
            res1 += 1

        # Part 2
        q = []
        for j in support_bricks[i]:
            if len(support[j]) == 1:
                q.append(j)
        falling = set(q)
        while q:
            idx = q.pop(0)
            for k in support_bricks[idx] - falling:
                if support[k] <= falling:
                    q.append(k)
                    falling.add(k)
        res2 += len(falling)

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
