## 2750. Ways to Split Array Into Good Subarrays

## You are given a binary array nums.
## A subarray of an array is good if it contains exactly one element with the value 1.
## Return an integer denoting the number of ways to split the array nums into good subarrays. As the number may be too large, return it modulo 109 + 7.
## A subarray is a contiguous non-empty sequence of elements within an array.

def numberOfGoodSubarraySplits(nums):
    pre=-1
    count=0
    for i in range(len(nums)):
        if nums[i]==1 and pre==-1:
            count=1
            pre=i
            continue
        elif nums[i]==1:
            count*=(i-pre)
            pre=i
    return count%(10**9+7)

def numberOfGoodSubarraySplits2(nums):
    pre=-1
    count=0
    for i in range(len(nums)):
        if nums[i]:
            if pre==-1:
                count=1
            else:
                count*=(i-pre)
            pre=i
    return count%(10**9+7)

if __name__=='__main__':
    nums=[0,1,0,0,1]
    print(numberOfGoodSubarraySplits(nums))