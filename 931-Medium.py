## 931. Minimum Falling Path Sum
from functools import reduce

def minFallingPathSum(matrix):
    pre_dp=matrix[0]
    dp=matrix[0].copy()
    n=len(matrix)
    for i in range(1,n):
        for j in range(n):
            min_i=max(j-1,0)
            min_pre=min(pre_dp[min_i:j+2])
            dp[j]=min_pre+matrix[i][j]
        pre_dp,dp=dp,pre_dp
    return min(pre_dp)

## inplace calculation
def minFallingPathSum2(matrix):
    n=len(matrix)
    for i in range(1,n):
        for j in range(n):
            min_i=max(j-1,0)
            min_pre=min(matrix[i-1][min_i:j+2])
            matrix[i][j]=min_pre+matrix[i][j]
    return min(matrix[-1])

## inplace calculation
def minFallingPathSum3(matrix):
    for i in range(1, len(matrix)):
        matrix[i]=[matrix[i][j]+min(matrix[i-1][max(j-1,0):j+2]) for j in range(len(matrix))]
    return min(matrix[-1])

## inplace calculation
def minFallingPathSum4(matrix):
    return min(reduce(lambda a,r: [q+min(a[max(0,j-1):j+2]) for j,q in enumerate(r)],matrix))


if __name__=='__main__':
    matrix = [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]
    print(minFallingPathSum4(matrix))