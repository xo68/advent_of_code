import os
import sys


def read_inputs():
    if not os.path.isfile("input.txt"):
        print("Input file input.txt does not exist!")
        sys.exit()
    with open("input.txt") as lines:
        return lines.readlines()


def main():
    res1, res2 = 0, 0

    for line in read_inputs():
        red, blue, green = 0, 0, 0
        game_possible = True

        line = line.split(" ")
        line.pop(0)

        game = int(line.pop(0).split(":")[0])  # GameID

        while line:
            count = int(line.pop(0))
            color = line.pop(0)

            if color.find("red") != -1:
                red = count if red < count else red
                game_possible = False if count > 12 else game_possible
            elif color.find("green") != -1:
                green = count if green < count else green
                game_possible = False if count > 13 else game_possible
            elif color.find("blue") != -1:
                blue = count if blue < count else blue
                game_possible = False if count > 14 else game_possible

        res1 += game if game_possible else 0
        res2 += red * blue * green

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")


if __name__ == "__main__":
    main()
