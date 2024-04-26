## 1289. Minimum Falling Path Sum II

def minFallingPathSum(grid):
    pre_dp=grid[0]
    dp=pre_dp.copy()
    n=len(grid)
    for i in range(1,n):
        for j in range(n):
            if j-1<0:
                left=0
            else:
                left=j
            min_pre=min(pre_dp[:left]+pre_dp[j+1:])
            dp[j]=min_pre+grid[i][j]
        pre_dp,dp=dp,pre_dp
    return min(pre_dp)












if __name__=='__main__':
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    print(minFallingPathSum(grid))