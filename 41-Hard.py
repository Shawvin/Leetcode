## 41. First Missing Positive

## Given an unsorted integer array nums, return the smallest missing positive integer.
## You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

def firstMissingPositive(nums):
    l=len(nums)
    i=0
    while (i<=l-1):
        if nums[i]>0 and nums[i]<=l and nums[nums[i]-1]!=nums[i]:
            nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        else:
            i+=1
    for i in range(l):
        if nums[i]!=i+1:
            return i+1
    return l+1

if __name__=='__main__':
    nums=[1,2,3,4,5]
    print(firstMissingPositive(nums))