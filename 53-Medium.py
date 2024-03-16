## 53. Maximum Subarray

## Given an integer array nums, find the subarray
##  with the largest sum, and return its sum.

def maxSubArray(nums):
    min_sum=nums[0]
    total=nums[0]
    max_sum=nums[0]
    for val in nums[1:]:
        total+=val
        max_sum=max(total, max_sum, total-min_sum)
        min_sum=min(total,min_sum)
    return max_sum

if __name__=='__main__':
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))