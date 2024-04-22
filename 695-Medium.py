## 695. Max Area of Island

## You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
## You may assume all four edges of the grid are surrounded by water.
## The area of an island is the number of cells with a value 1 in the island. 
## Return the maximum area of an island in grid. If there is no island, return 0.

def maxAreaOfIsland(grid):
    def dfs(i,j,grid):
        count=1
        grid[i][j]=0
        if i>0 and grid[i-1][j]==1:
            count+=dfs(i-1,j,grid)
        if j>0 and grid[i][j-1]==1:
            count+=dfs(i,j-1,grid)
        if i<len(grid)-1 and grid[i+1][j]==1:
            count+=dfs(i+1,j,grid)
        if j<len(grid[0])-1 and grid[i][j+1]==1:
            count+=dfs(i,j+1,grid)
        return count
    max_count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                max_count=max(max_count, dfs(i,j,grid))
    return max_count

if __name__=='__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(maxAreaOfIsland(grid))