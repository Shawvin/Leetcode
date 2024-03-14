## 2485. Find the Pivot Integer

## Given a positive integer n, find the pivot integer x such that:
## 
## The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
## Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

def pivotInteger(n):
    pre=0
    all_sum=(1+n)*n/2
    for i in range(1,n+1):
        cur=pre+i
        if all_sum-pre==cur:
            return i
        if all_sum-pre<cur:
            return -1
        pre=cur

if __name__=='__main__':
    n=8
    print(pivotInteger(n))