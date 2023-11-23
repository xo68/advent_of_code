import os
import re
import sys

FILE = "input.txt"


def read_inputs() -> list:
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()
    with open(FILE) as lines:
        return lines.readlines()


map = []
visited = []
to_explore = []
len_path, mapX, mapY = 0, 0, 0
S, E = (), ()


def already_visited(pos):
    for i in visited:
        if i == pos:
            return True
    visited.append(pos)
    return False


def check_paths(pos):
    global to_explore
    x, y, h = pos

    if x + 1 < mapX:
        if map[x + 1][y] <= map[x][y] or map[x + 1][y] == map[x][y] + 1:
            new_pos = (x + 1, y, map[x + 1][y])
            if not already_visited(new_pos):
                to_explore.append(new_pos)

    if x - 1 >= 0:
        if map[x - 1][y] <= map[x][y] or map[x - 1][y] == map[x][y] + 1:
            new_pos = (x - 1, y, map[x - 1][y])
            if not already_visited(new_pos):
                to_explore.append(new_pos)

    if y + 1 < mapY:
        if map[x][y + 1] <= map[x][y] or map[x][y + 1] == map[x][y] + 1:
            new_pos = (x, y + 1, map[x][y + 1])
            if not already_visited(new_pos):
                to_explore.append(new_pos)

    if y - 1 >= 0:
        if map[x][y - 1] <= map[x][y] or map[x][y - 1] == map[x][y] + 1:
            new_pos = (x, y - 1, map[x][y - 1])
            if not already_visited(new_pos):
                to_explore.append(new_pos)


def explore(start):
    global visited, to_explore
    visited = []
    to_explore = []
    len_path = 0
    found = False

    to_explore.append(start)

    while not found:
        tmp_explore = to_explore[:]
        to_explore = []
        while tmp_explore:
            node = tmp_explore.pop()
            check_paths(node)
            if node == E:
                return len_path
        len_path += 1
        if not to_explore:
            return 9999


def load_map():
    global S, E, map, mapY, mapX
    tmp = list()
    input = read_inputs()

    for i, line in enumerate(input):
        tmp.append(list(line.strip()))

    mapY = len(tmp)
    mapX = len(tmp[0])

    for x in range(mapX):
        map.append([])
        for y in range(mapY):
            if tmp[y][x] == "S":
                S = (x, y, ord("a"))
                map[x].append(ord("a"))
            elif tmp[y][x] == "E":
                E = (x, y, ord("z"))
                map[x].append(ord("z"))
            else:
                map[x].append(ord(tmp[y][x]))


def proceed():
    print(f"Result part 1 = {explore(S)}")

    len = 9999
    for x in range(mapX):
        for y in range(mapY):
            if map[x][y] == ord("a"):
                dist = explore((x, y, map[x][y]))
                if dist < len:
                    len = dist
    print(f"Result part 2 = {len}")


if __name__ == "__main__":
    load_map()
    proceed()
