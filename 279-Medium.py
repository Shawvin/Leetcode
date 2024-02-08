## 279. Perfect Squares

## Given an integer n, return the least number of perfect square numbers that sum to n.

## A perfect square is an integer that is the square of an integer; in other words, it is 
## the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

## dp
import math

def numSquares(n):
    dp=[0]*(n+1)
    for i in range(1,n+1):
        min_value=float('inf')
        for j in range(1,int(math.sqrt(i))+1):
            min_value=min(min_value, dp[i-j*j]+1)
        dp[i]=min_value
        print(dp[i])
    return dp[n]

if __name__=='__main__':
    n=13
    print(numSquares(n))