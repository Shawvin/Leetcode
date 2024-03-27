## 713. Subarray Product Less Than K

## Given an array of integers nums and an integer k, return the number of contiguous subarrays 
## where the product of all the elements in the subarray is strictly less than k.

## sliding window
def numSubarrayProductLessThanK(nums, k):
    prod=1
    j=0
    count=0
    for i in range(len(nums)):
        prod*=nums[i]
        while prod>=k and j<i:
            prod=prod/nums[j]
            j+=1
        if prod<k:
            count+=(i-j+1)
    return count

def numSubarrayProductLessThanK2(nums, k):
    prod, left, count=1,0,0
    for right in range(len(nums)):
        prod*=nums[right]
        while prod>=k and right>=left:
            prod/=nums[left]
            left+=1
        count+=right-left+1
    return count

if __name__=='__main__':
    nums = [10,5,2,6]
    k=100
    print(numSubarrayProductLessThanK(nums, k))