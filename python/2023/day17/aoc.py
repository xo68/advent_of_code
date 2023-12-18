from heapq import heappop, heappush

DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))  # (ROW,COLUMN)

# PART 1
# MIN_LIMIT = 1
# MAX_LIMIT = 3


# PART 2
MIN_LIMIT = 4
MAX_LIMIT = 10

if __name__ == "__main__":
    queue = [(0, 0, 0, 0, 0, 0)]  # (heat_loss,row,col,dir_row,dir_col,number)
    res = 0
    visited = set()

    G = []
    for rg in open("input.txt").read().strip().split("\n"):
        G.append(list(map(int, rg)))

    ROW = len(G)
    COL = len(G[0])

    while queue:
        heat_loss, row, col, dir_row, dir_col, num = heappop(queue)

        if row == ROW - 1 and col == COL - 1 and num >= MIN_LIMIT:
            res = heat_loss
            break

        if (row, col, dir_row, dir_col, num) not in visited:
            visited.add((row, col, dir_row, dir_col, num))

            if num < MAX_LIMIT and (dir_row, dir_col) != (0, 0):
                r = row + dir_row
                c = col + dir_col
                if r >= 0 and r < ROW and c >= 0 and c < COL:
                    h = heat_loss + G[r][c]
                    n = num + 1
                    heappush(queue, (h, r, c, dir_row, dir_col, n))

            if num >= MIN_LIMIT or (dir_row, dir_col) == (0, 0):
                for dr, dc in DIRECTIONS:
                    if (dr, dc) != (dir_row, dir_col) and (dr, dc) != ( -dir_row, -dir_col,):
                            r = row + dr
                        c = col + dc
                        if r >= 0 and r < ROW and c >= 0 and c < COL:
                            h = heat_loss + G[r][c]
                            heappush(queue, (h, r, c, dr, dc, 1))

    print(f"Result:{res}")
