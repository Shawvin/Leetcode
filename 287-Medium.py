## 287. Find the Duplicate Number

## Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
## There is only one repeated number in nums, return this repeated number.
## You must solve the problem without modifying the array nums and uses only constant extra space.

def findDuplicate(nums):
    i=0
    n=len(nums)
    while i<n:
        if nums[i]<n and nums[nums[i]-1]!=nums[i]:
            nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        else:
            i+=1
    for j in range(n):
        if nums[j]!=j+1:
            return nums[j]
        
if __name__=='__main__':
    nums=[1,3,4,2,2]
    print(findDuplicate(nums))