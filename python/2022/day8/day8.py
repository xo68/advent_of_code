import os
import sys

FILE = "input.txt"

# https://adventofcode.com/2022/day/8


class Tree:
    def __init__(self, height):
        self.h = height
        # Part2 - Visible Trees left, right, up, down
        self.l = 0
        self.r = 0
        self.u = 0
        self.d = 0

    def scenic_score(self):
        return self.l * self.r * self.u * self.d


class Forest:
    def __init__(self, file):
        self.visible_trees = 0
        with open(file) as lines:
            line = lines.read().splitlines()
            self.grid = [[Tree(int(height)) for height in item] for item in line]
            self.grid_size = len(self.grid[0])

    def get_visible_trees(self):
        return self.visible_trees

    def display(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                print(f"Tree:{i}:{j}={self.grid[i][j].h}")

    def calculate_visible_trees(self):
        self.visible_trees = 0
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                visible = False
                t = self.grid[i][j]
                if self.__tree_visible_from_top(t, i, j):
                    visible = True
                if self.__tree_visible_from_bottom(t, i, j):
                    visible = True
                if self.__tree_visible_from_left(t, i, j):
                    visible = True
                if self.__tree_visible_from_right(t, i, j):
                    visible = True
                if visible:
                    self.visible_trees += 1
                t.scenic_score()

    def __tree_visible_from_top(self, tree, i, j):
        for ii in range(i):
            tt = self.grid[i - ii - 1][j]
            tree.u += 1
            if tt.h >= tree.h:
                return False
        return True

    def __tree_visible_from_left(self, tree, i, j):
        for jj in range(j):
            tt = self.grid[i][j - jj - 1]
            tree.l += 1
            if tt.h >= tree.h:
                return False
        return True

    def __tree_visible_from_bottom(self, tree, i, j):
        for ii in range(self.grid_size - i - 1):
            tt = self.grid[i + ii + 1][j]
            tree.d += 1
            if tt.h >= tree.h:
                return False
        return True

    def __tree_visible_from_right(self, tree, i, j):
        for jj in range(self.grid_size - j - 1):
            tt = self.grid[i][j + jj + 1]
            tree.r += 1
            if tt.h >= tree.h:
                return False
        return True

    def get_highest_scenic_score(self):
        score = 0
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                current = self.grid[i][j].scenic_score()
                if current > score:
                    score = current
        return score


def main():
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()

    forest = Forest(FILE)
    # forest.display()
    forest.calculate_visible_trees()
    print(f"Part1 - Visible Tree = {forest.get_visible_trees()}")
    print(f"Part2 - Scenic Scope = {forest.get_highest_scenic_score()}")


if __name__ == "__main__":
    main()
