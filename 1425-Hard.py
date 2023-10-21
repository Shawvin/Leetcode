## 1425. Constrained Subsequence Sum

## Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of 
## that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], 
## where i < j, the condition j - i <= k is satisfied.

import collections

def constrainedSubsetSum(nums, k):
    result=[0]*len(nums)
    result[0]=nums[0]
    global_max=result[0]
    deque = collections.deque()
    deque.append(result[0])
    for i in range(1,len(nums)):
        local_max=deque[0] if deque else 0
        local_max=max(0, local_max)
        result[i]=local_max+nums[i]
        while len(deque) and result[i]>deque[-1]:
            deque.pop()
        deque.append(result[i])
        if i>=k and deque and deque[0]==result[i-k]:
            deque.popleft()
        global_max=max(result[i], global_max)
    return global_max

if __name__=='__main__':
    nums=[10,2,-10,5,20]
    k = 2
    print(constrainedSubsetSum(nums,k))