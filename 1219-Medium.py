## 1219. Path with Maximum Gold

def getMaximumGold(grid):
    def backtracking(i,j, grid):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
            return 0
        cur=grid[i][j]
        grid[i][j]=0
        max_gold=0
        for change in (-1,1):
            max_gold=max(max_gold, cur+backtracking(i+change,j,grid))
            max_gold=max(max_gold, cur+backtracking(i,j+change,grid))
        grid[i][j]=cur
        return max_gold
    
    max_gold=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                max_gold=max(max_gold,backtracking(i,j, grid))
    return max_gold

if __name__=='__main__':
    grid = [[0,6,0],[5,8,7],[0,9,0]]
    print(getMaximumGold(grid))