## 1043. Partition Array for Maximum Sum

## Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. 
## After partitioning, each subarray has their values changed to become the maximum value of that subarray.
## Return the largest sum of the given array after partitioning.

## dp
def maxSumAfterPartitioning(arr,k):
    l=len(arr)
    if l<=k:
        return max(arr)*l
    else:
        result=[0]*l
        for i in range(k):
            result[i]=max(arr[:i+1])*(i+1)
        for i in range(k,l):
            for j in range(1,k+1):
                result[i]=max(result[i], result[i-j]+max(arr[i-j+1:i+1])*j)
    return result[-1]

def maxSumAfterPartitioning2(arr,k):
    l=len(arr)
    if l<=k:
        return max(arr)*l
    else:
        result=[0]*l
        curr_max=0
        for i in range(k):
            curr_max=max(curr_max, arr[i])
            result[i]=curr_max*(i+1)
        for i in range(k,l):
            curr_max=arr[i]
            for j in range(1,k+1):
                curr_max=max(curr_max,arr[i-j+1])
                result[i]=max(result[i], result[i-j]+curr_max*j)
    return result[-1]
    
if __name__=='__main__':
    arr=[1,4,1,5,7,3,6,1,9,9,3]
    k=4
    print(maxSumAfterPartitioning2(arr,k))