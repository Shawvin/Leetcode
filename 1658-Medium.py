## 1658. Minimum Operations to Reduce X to Zero

## You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element 
## from the array nums and subtract its value from x. Note that this modifies the array for future operations.

def minOperations(nums, x):
    total=sum(nums)
    if total<x:
        return -1
    if total==x:
        return len(nums)
    target=total-x
    start=0
    cumsum=0
    array_len=0
    for i in range(0,len(nums)):
        cumsum+=nums[i]
        while(cumsum>target and start<=i):
            cumsum-=nums[start]
            start+=1
        if cumsum==target:
            array_len=max(i-start+1, array_len)
    if array_len>0:
        return len(nums)-array_len
    return -1

if __name__=='__main__':
    nums=[3,2,20,1,1,3]
    x=10
    print(minOperations(nums, x))