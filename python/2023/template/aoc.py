import os
import re
import sys

# digits = re.compile(r"[1-9]")
# values = "one|two|three|four|five|six|seven|eight|nine|[1-9]"
# all = re.compile(values)  # Return all matches that are non-overlap
# last = re.compile(r"(?:.*)(" + values + ")")  # Return only the last match
# val1 = all.findall(line)[0]
# var = re.compile(r"(Exp)(Exp)")
# var.match("data")
# var.match("data").group(X)

# [row][column]
# data = [[0 for _ in range(COLUMN)] for _ in range(ROW)]


if __name__ == "__main__":
    res1, res2 = 0, 0

    lines = open("input.txt").read().strip().split("\n")
    for line in lines:
        print(line)
        # print(list(line))

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
