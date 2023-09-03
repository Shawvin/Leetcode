## 62. Unique Paths

## There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
## The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
## Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

def uniquePaths(m, n):
        ways=[0]*n
        ways[0]=1
        for i in range(m):
            for j in range(n):
                if j-1>=0:
                    ways[j]+=ways[j-1]
        return ways[-1]


if __name__=='__main__':
     m=3
     n=7
     print(uniquePaths(m,n))