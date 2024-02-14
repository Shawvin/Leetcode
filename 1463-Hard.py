## 1463. Cherry Pickup II

## You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.
## You have two robots that can collect cherries for you:

## Robot #1 is located at the top-left corner (0, 0), and
## Robot #2 is located at the top-right corner (0, cols - 1).
## Return the maximum number of cherries collection using both robots by following the rules below:

## From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
## When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
## When both robots stay in the same cell, only one takes the cherries.
## Both robots cannot move outside of the grid at any moment.
## Both robots should reach the bottom row in grid.

def cherryPickup(grid):
    rows=len(grid)
    cols=len(grid[0])
    dp=[[[0,0] for j in range(cols)] for i in range(rows)]
    dp[0][0][0]=grid[0][0]
    dp[0][cols-1][1]=grid[0][cols-1]
    for i in range(1,rows):
        for j in range(cols):
            if j==0:
                max_pre1=max(dp[i-1][j][0],dp[i-1][j+1][0])
                max_pre2=max(dp[i-1][j][1],dp[i-1][j+1][1])
                if max_pre1==0:
                    dp[i][j][0]=0
                else:
                    dp[i][j][0]=max_pre1+grid[i][j]
                if max_pre2==0:
                    dp[i][j][1]=0
                else:
                    dp[i][j][1]=max_pre2+grid[i][j]
            elif j==cols-1:
                max_pre1=max(dp[i-1][j-1][0],dp[i-1][j][0])
                max_pre2=max(dp[i-1][j-1][1],dp[i-1][j][1])
                if max_pre1==0:
                    dp[i][j][0]=0
                else:
                    dp[i][j][0]=max_pre1+grid[i][j]
                if max_pre2==0:
                    dp[i][j][1]=0
                else:
                    dp[i][j][1]=max_pre2+grid[i][j]
            else:
                max_pre1=max(dp[i-1][j-1][0],dp[i-1][j][0],dp[i-1][j+1][0])
                max_pre2=max(dp[i-1][j-1][1],dp[i-1][j][1],dp[i-1][j+1][1])
                if max_pre1==0:
                    dp[i][j][0]=0
                else:
                    dp[i][j][0]=max_pre1+grid[i][j]
                if max_pre2==0:
                    dp[i][j][1]=0
                else:
                    dp[i][j][1]=max_pre2+grid[i][j]
        print(dp)
    max1=0
    max2=0
    for j in range(cols):
        max1=max(dp[rows-1][j][0],max1)
        max2=max(dp[rows-1][j][1],max2)
    return max1+max2

if __name__=='__main__':
    grid=[[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
    print(cherryPickup(grid))