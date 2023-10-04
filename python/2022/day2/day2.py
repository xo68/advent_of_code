import os
import sys

# A, X = "Rock", "Rock"
# B, Y = "Paper", "Paper"
# C, Z = "Scissors", "Scissors"
# PART2 ->
# X means you need to lose,
# Y means you need to end the round in a draw,
# Z means you need to win.

FILE = "input.txt"

LOST = 0
DRAW = 3
WIN = 6

ROCK = 1
PAPER = 2
SCISSOR = 3


def main():
    total, total2 = 0, 0
    p1, p2 = "", ""

    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()

    with open(FILE) as f:
        lines = f.readlines()

    # P2 is the player in scope
    for line in lines:
        game = line.split()
        p1 = game[0]

        # Check for what you play
        if game[1] == "X":
            total = total + 1
            total2 = total2 + LOST
            p2 = "A"
        elif game[1] == "Y":
            total = total + 2
            total2 = total2 + DRAW
            p2 = "B"
        else:
            total = total + 3
            total2 = total2 + WIN
            p2 = "C"

        # Part 1
        # Check for DRAW / WIN / LOST
        if p1 == p2:
            total = total + DRAW
        elif p2 == "A" and p1 == "B":
            total = total + LOST
        elif p2 == "A" and p1 == "C":
            total = total + WIN
        elif p2 == "B" and p1 == "A":
            total = total + WIN
        elif p2 == "B" and p1 == "C":
            total = total + LOST
        elif p2 == "C" and p1 == "A":
            total = total + LOST
        elif p2 == "C" and p1 == "B":
            total = total + WIN
        else:
            print("UNKNOWN")

        # Part 2
        # End in Draw
        if p2 == "B":
            if p1 == "A":
                total2 = total2 + 1
            if p1 == "B":
                total2 = total2 + 2
            if p1 == "C":
                total2 = total2 + 3
        # End in Win
        if p2 == "C":
            if p1 == "A":
                total2 = total2 + 2
            if p1 == "B":
                total2 = total2 + 3
            if p1 == "C":
                total2 = total2 + 1
        # End in Lose
        if p2 == "A":
            if p1 == "A":
                total2 = total2 + 3
            if p1 == "B":
                total2 = total2 + 1
            if p1 == "C":
                total2 = total2 + 2

    print(f"Total Part1:{total}")
    print(f"Total Part2:{total2}")


if __name__ == "__main__":
    main()
