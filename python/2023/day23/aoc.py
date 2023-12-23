import sys

sys.setrecursionlimit(10000)
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
TILES = ".<>^v"
results1 = set()
results2 = set()


# Part 1 - Deep Search
# Brute force -> 1.5 seconds, OK ;)
def dfs(next, seen=[], direction="v"):
    r, c = next
    if (r, c) == (END[0], END[1]):
        results1.add(len(seen))
    else:
        seen.append((r, c))
        if c + 1 < COL and grid[r][c + 1] in ".>":
            if (r, c + 1) not in seen:
                dfs((r, c + 1), seen[:], ">")
        if c - 1 >= 0 and grid[r][c - 1] in "<.":
            if (r, c - 1) not in seen:
                dfs((r, c - 1), seen[:], "<")
        if r - 1 >= 0 and grid[r - 1][c] in ".^":
            if (r - 1, c) not in seen:
                dfs((r - 1, c), seen[:], "^")
        if r + 1 < ROW and grid[r + 1][c] in ".v":
            if (r + 1, c) not in seen:
                dfs((r + 1, c), seen[:], "v")


# Part2 - Solution 1, Deep Search
# Brute Force -> it was running while searching for a better solution :)
def dfs2(next, seen=[]):
    r, c = next
    if (r, c) == (END[0], END[1]):
        results2.add(len(seen))
    else:
        seen.append((r, c))
        if r - 1 >= 0 and grid[r - 1][c] in TILES and (r - 1, c) not in seen:
            dfs2((r - 1, c), seen[:])
        if c - 1 >= 0 and grid[r][c - 1] in TILES and (r, c - 1) not in seen:
            dfs2((r, c - 1), seen[:])
        if c + 1 < COL and grid[r][c + 1] in TILES and (r, c + 1) not in seen:
            dfs2((r, c + 1), seen[:])
        if r + 1 < ROW and grid[r + 1][c] in TILES and (r + 1, c) not in seen:
            dfs2((r + 1, c), seen[:])


# Part2 - Solution 2, create a weighted Tree
# No need to browse the full grid
# TODO: Currently broken, under rewrite
def sol2():
    # Get all the nodes of the target graph
    graph = [START, END]
    for r, row in enumerate(grid):
        for c, tile in enumerate(row):
            if tile in TILES:
                n = 0
                for ri, ci in DIRECTIONS:
                    nr = r + ri
                    nc = c + ci
                    if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] in TILES:
                        n += 1
                if n > 2:
                    graph.append((r, c))

    # Connect all nodes & store distances
    # node = Node(START[0], START[1])
    for r, c in graph.keys():
        stack = [(r, c, 0)]
        seen = [(r, c)]

        while stack:
            ri, ci, di = stack.pop()
            if di != 0 and (ri, ci) in graph:
                graph[(r, c)] += [(ri, ci, di)]
                continue

            for ru, cu in DIRECTIONS:
                nr = ri + ru
                nc = ci + cu
                if (
                    0 <= nr < ROW
                    and 0 <= nc < COL
                    and grid[nr][nc] in TILES
                    and (nr, nc) not in seen
                ):
                    seen.append((nr, nc))
                    stack.append((nr, nc, di + 1))


if __name__ == "__main__":
    res1, res2 = 0, 0
    grid = []
    lines = open("input.txt").read().strip().split("\n")
    for line in lines:
        grid.append(list(line))

    ROW = len(grid)
    COL = len(grid[0])
    START = (0, 1)
    END = (ROW - 1, COL - 2)

    # Part 1
    dfs(START)
    res1 = max(results1)
    print(f"Result1:{res1}")

    # Part 2
    dfs2(START)
    res2 = max(results2)
    print(f"Result2:{res2}")
