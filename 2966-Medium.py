## 2966. Divide Array Into Arrays With Max Difference

## You are given an integer array nums of size n and a positive integer k.

## Divide the array into one or more arrays of size 3 satisfying the following conditions:
## 
## Each element of nums should be in exactly one array.
## The difference between any two elements in one array is less than or equal to k.

def divideArray(nums, k):
    result=[]
    nums=sorted(nums)
    l=len(nums)
    for i in range(0,l,3):
        if nums[i+2]-nums[i]>k:
            return []
        else:
            result.append(nums[i:i+3])
    return result

if __name__=='__main__':
    nums=[1,3,4,8,7,9,3,5,1]
    k=2
    print(divideArray(nums, k))