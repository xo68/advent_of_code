import re
import sys

if __name__ == "__main__":
    res1, res2 = 10000000000, 10000000000
    lines = open("input.txt").read().split("\n")

    comp = []  # table of tables of tuples
    tmp = []  # list of tuples (dest, start, range)

    # Load all data
    all_seeds = [int(x) for x in lines.pop(0).split(":")[1].split()]
    for line in lines:
        if not line:
            if tmp:
                comp.append(tmp[:])
                tmp.clear()
        elif line[0].isdigit():
            d, s, r = map(int, line.split())
            tmp.append((d, s, r))

    # Part 1
    for seed in all_seeds:
        for all_comp in comp:
            for ss in all_comp:
                if seed >= ss[1] and seed < ss[1] + ss[2]:
                    seed = ss[0] + seed - ss[1]
                    break
        res1 = seed if seed < res1 else res1

    # Part 2
    for i in range(0, len(all_seeds), 2):
        for seed in range(all_seeds[i], all_seeds[i] + all_seeds[i + 1]):
            for pid, all_comp in enumerate(comp):
                for pos, ss in enumerate(all_comp):
                    if seed >= ss[1] and seed < ss[1] + ss[2]:
                        seed = ss[0] + seed - ss[1]
                        break
            if seed < res2:
                res2 = seed

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
