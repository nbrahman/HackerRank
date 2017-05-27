surroundingCellRowCols = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

def getBiggestRegion(i, j, grid, mark, color):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return

    if grid[i][j] == 0:
        return

    if mark[i][j] != -1:
        return

    mark [i][j] = color
    for s in surroundingCellRowCols:
        getBiggestRegion(i + s[0], j + s[1], grid, mark, color)


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
mark = [[-1]* m for i in range(n)]
c = 0
for i in range(n):
    for j in range(m):
        getBiggestRegion (i, j, grid, mark, c)
        c += 1
count = [0] * (n * m)
for i in range(n):
    for j in range(m):
        if mark[i][j] != -1:
            count[mark[i][j]] += 1
print(max(count))
