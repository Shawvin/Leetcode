## 200. Number of Islands

## Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
## An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

def numIslands(grid):
    def dfs(i, j, grid):
        if i > 0 and grid[i - 1][j] == '1':
            grid[i - 1][j] = 0
            dfs(i - 1, j, grid)
        if j > 0 and grid[i][j - 1] == '1':
            grid[i][j - 1] = 0
            dfs(i, j - 1, grid)
        if i < len(grid) - 1 and grid[i + 1][j] == '1':
            grid[i + 1][j] = 0
            dfs(i + 1, j, grid)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
            grid[i][j + 1] = 0
            dfs(i, j + 1, grid)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j, grid)
    return count

if __name__=='__main__':
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    print(numIslands(grid))