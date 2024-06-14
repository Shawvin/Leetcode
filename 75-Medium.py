## 75. Sort Colors

## Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
## We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
## You must solve this problem without using the library's sort function.

# bubble sort
def sortColors(nums):
    for j in range(len(nums)-1,0,-1):
        for i in range(j):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
    return nums

# selection sort
def sortColors2(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    return nums

# window sort
def sortColors3(nums):
    i=0
    j=0
    k=len(nums)-1
    while j<=k:
        if nums[j]==0:
            nums[j],nums[i]=nums[i],nums[j]
            i+=1
            j+=1
        elif nums[j]==1:
            j+=1
        else:
            nums[k],nums[j]=nums[j],nums[k]
            k-=1
    return nums

# list comprehension
def sortColors4(nums):
    res=[0,0,0]
    for num in nums:
        res[num]+=1
    count=0
    for i in range(3):
        for j in range(res[i]):
            nums[count]=i
            count+=1
    return nums
          
if __name__=='__main__':
    nums=[1,2,2]
    print(sortColors4(nums))