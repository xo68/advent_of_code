import os
import sys

FILE = "input.txt"

# https://adventofcode.com/2022/day/9


class Motions:
    def __init__(self, file):
        self.rope = [[0, 0] for _ in range(10)]
        self.tpos = set()  # list of all unique tail positions - part1
        self.tpos2 = set()  # list of all unique tail positions - part 2
        self.motions = list()  # Motions from input file
        with open(file) as lines:
            for line in lines:
                motion = line.split()
                self.motions.append(motion)

    def display(self):
        for motion in self.motions:
            print(f"Motions:{motion}")

    # Loop through all the rows
    def process(self):
        for motion in self.motions:
            self.__trigger_move(motion[0], int(motion[1]))

    # Process 1 row -> d: Direction; m: Amount
    def __trigger_move(self, d, m):
        for _ in range(m):
            x = 1 if d == "R" else -1 if d == "L" else 0
            y = 1 if d == "U" else -1 if d == "D" else 0
            self.rope[0][0] += x
            self.rope[0][1] += y

            for i in range(9):
                head = self.rope[i]
                tail = self.rope[i + 1]

                _x = head[0] - tail[0]
                _y = head[1] - tail[1]

                if abs(_x) > 1 or abs(_y) > 1:
                    if _x == 0:
                        tail[1] += _y // 2
                    elif _y == 0:
                        tail[0] += _x // 2
                    else:
                        tail[0] += 1 if _x > 0 else -1
                        tail[1] += 1 if _y > 0 else -1
            self.tpos.add(tuple(self.rope[1]))
            self.tpos2.add(tuple(self.rope[-1]))


def main():
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()

    motions = Motions(FILE)
    motions.process()
    print(f"part1: {len(motions.tpos)}")
    print(f"part2: {len(motions.tpos2)}")


if __name__ == "__main__":
    main()
