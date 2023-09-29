## 905. Sort Array By Parity

## Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

def sortArrayByParity(nums):
    i=0
    j=len(nums)-1
    while True:
        while nums[i]%2==0 and i<(len(nums)-1):
            i+=1
        while nums[j]%2==1 and j>0:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
        else:
            break
    return nums


def sortArrayByParity2(nums):
    odd=0
    even=0
    while even<len(nums):
        while nums[even]%2==1 and even<(len(nums)-1):
            even+=1
        nums[even], nums[odd]=nums[odd], nums[even]
        even+=1
        odd+=1
    return nums

def sortArrayByParity3(nums):
    odd=0
    for i in range(len(nums)):
        if nums[i]%2==0:
            nums[i], nums[odd]=nums[odd], nums[i]
            odd+=1
    return nums

if __name__=='__main__':
    nums = [3,1,2,4]
    print(sortArrayByParity3(nums))
