## 2149. Rearrange Array Elements by Sign

## You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
## You should rearrange the elements of nums such that the modified array follows the given conditions:
## Every consecutive pair of integers have opposite signs.
## For all integers with the same sign, the order in which they were present in nums is preserved.
## The rearranged array begins with a positive integer.
## Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

## two subarray
def rearrangeArray(nums):
    nums_p=[]
    nums_n=[]
    for num in nums:
        if num>0:
            nums_p.append(num)
        else:
            nums_n.append(num)
    for i in range(len(nums)):
        if i%2==0:
            nums[i]=nums_p[i//2]
        else:
            nums[i]=nums_n[(i-1)//2]
    return nums

## two pointer
def rearrangeArray2(nums):
    n=len(nums)
    po,ne=0,1
    result=[0]*n
    for i in range(n):
        if nums[i]>0:
            result[po]=nums[i]
            po+=2
        else:
            result[ne]=nums[i]
            ne+=2
    return result

if __name__=='__main__':
    nums = [3,1,-2,-5,2,-4]
    print(rearrangeArray(nums))