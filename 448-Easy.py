## 448. Find All Numbers Disappeared in an Array

## Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbers(nums):
    i=0
    while i<len(nums):
        if nums[i]-1!=i and nums[nums[i]-1]!=nums[i]:
            nums[nums[i]-1], nums[i]= nums[i], nums[nums[i]-1]
        else:
            i+=1
    res=[]
    for i in range(len(nums)):
        if nums[i]!=i+1:
            res.append(i+1)
    return res

def findDisappearedNumbers2(nums):
    for i in range(len(nums)):
        j=abs(nums[i])
        if nums[j-1]>0:
            nums[j-1]*=-1
    res=[]
    for i in range(len(nums)):
        if nums[i]>0:
            res.append(i+1)
    return res

if __name__=='__main__':
    nums=[4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(nums))