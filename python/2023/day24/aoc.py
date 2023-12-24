import re

from sympy import Line, Point, solve, symbols

# MIN = 7
# MAX = 27
MIN = 200000000000000
MAX = 400000000000000


def intersect(h1, h2):
    h1p1, h1p2 = Point(h1[0], h1[1]), Point(h1[0] + h1[3], h1[1] + h1[4])
    h2p1, h2p2 = Point(h2[0], h2[1]), Point(h2[0] + h2[3], h2[1] + h2[4])
    l1 = Line(h1p1, h1p2)
    l2 = Line(h2p1, h2p2)
    pl = l1.intersection(l2)
    if pl:
        point = pl.pop()
        return (float(point[0]), float(point[1]))
    else:
        None


def in_future(h1, h2, x, y):
    if (x - h1[0]) * h1[3] >= 0 and (y - h1[1]) * h1[4]:
        if (x - h2[0]) * h2[3] >= 0 and (y - h2[1]) * h2[4]:
            return True
    return False


if __name__ == "__main__":
    res1, res2 = 0, 0
    H = []
    lines = open("input.txt").read().strip().split("\n")
    for line in lines:
        (
            x,
            y,
            z,
            vx,
            vy,
            vz,
        ) = re.findall("[-0-9]+", line)
        H.append(list(map(int, [x, y, z, vx, vy, vz])))

    # Part 1
    for i in range(len(H)):
        for j in range(i + 1, len(H)):
            h1, h2 = H[i], H[j]
            pt = intersect(h1, h2)
            if pt:
                x, y = pt
                if MIN <= x <= MAX and MIN <= y <= MAX and in_future(h1, h2, x, y):
                    res1 += 1

    # Part 2

    # Rock symbols for the equations
    xr, yr, zr, vxr, vyr, vzr = symbols("xr, yr, zr, vxr, vyr, vzr")

    # 2 equations required
    # We can skip the implicit third equation
    # Transform the equations as sympy will solve eq = 0
    # xr - x      yr - y      zr - r
    # --------- = --------- = --------
    # vx - vxr    vy - vyr    vz - vzr

    eq = []
    for x, y, z, vx, vy, vz in H:
        eq.append((xr - x) * (vy - vyr) - (yr - y) * (vx - vxr))
        eq.append((yr - y) * (vz - vzr) - (zr - z) * (vy - vyr))

    res = solve(eq)[0]
    res2 = res[xr] + res[yr] + res[zr]

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
