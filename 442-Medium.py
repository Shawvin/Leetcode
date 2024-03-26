## 442. Find All Duplicates in an Array

## Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer 
## appears once or twice, return an array of all the integers that appears twice.
## 
## You must write an algorithm that runs in O(n) time and uses only constant extra space.

def findDuplicates(nums):
    res=set()
    for i in range(len(nums)):
        while True:
            print(nums)
            print(res)
            if nums[i]-1!=i and nums[nums[i]-1]==nums[i]:
                res.add(nums[i])
                break
            elif nums[i]-1==i:
                break
            else:
                temp=nums[i]
                nums[i]=nums[temp-1]
                nums[temp-1]=temp
    return list(res)

def findDuplicates2(nums):
    res=[]
    for i in range(len(nums)):
        x=abs(nums[i])
        if nums[x-1]<0:
            res.append(x)
        nums[x-1]*=-1
    return res

if __name__=='__main__':
    nums=[4,3,2,7,8,2,3,1]
    #findDuplicates(nums)
    print(findDuplicates(nums))