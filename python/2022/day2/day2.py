import os
import sys

# A, X = "Rock", "Rock"
# B, Y = "Paper", "Paper"
# C, Z = "Scissors", "Scissors"

FILE = "input.txt"
LOST = 0
DRAW = 3
WIN = 6


def main():
    total = 0
    p1 = ""
    p2 = ""

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
            p2 = "A"
        elif game[1] == "Y":
            total = total + 2
            p2 = "B"
        else:
            total = total + 3
            p2 = "C"

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

    print(f"Total:{total}")


if __name__ == "__main__":
    main()
