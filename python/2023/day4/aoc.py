import os
import re
import sys


def read_inputs():
    FILE = "input.txt"
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()
    with open(FILE) as lines:
        return lines.readlines()


def main():
    res1, res2 = 0, 0
    res2_tab = [int(0) for _ in range(193)]

    for card, line in enumerate(read_inputs()):
        card_id = card + 1
        left_str, right_str = line.rstrip().split("|")
        left = set(re.findall(r"\d+", left_str)[1:])
        right = set(re.findall(r"\d+", right_str))

        res1 += int(pow(2, (len(left & right) - 1)))

        res2_tab[card_id] += 1
        for _ in range(res2_tab[card_id]):
            for next in range(len(left & right)):
                res2_tab[card_id + next + 1] += 1
        res2 += res2_tab[card_id]

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")


if __name__ == "__main__":
    main()
