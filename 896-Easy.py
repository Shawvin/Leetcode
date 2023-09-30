## 896. Monotonic Array

## An array is monotonic if it is either monotone increasing or monotone decreasing.
## An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
## Given an integer array nums, return true if the given array is monotonic, or false otherwise.

def isMonotonic(nums):
    if len(nums)==1:
        return True
    pre=nums[0]
    total_diff=0
    for i in nums:
        if total_diff*(i-pre)<0:
            return False
        total_diff+=(i-pre)
        pre=i
    return True

if __name__=='__main__':
    nums = [6,5,4,4]
    print(isMonotonic(nums))