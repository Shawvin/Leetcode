## 560. Subarray Sum Equals K

## Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
## A subarray is a contiguous non-empty sequence of elements within an array.

def subarraySum(nums, k):
    total=0
    sum_dict={}
    sum_dict[0]=1
    count=0
    for i in range(len(nums)):
        total+=nums[i]
        if total-k in sum_dict:
            count+=sum_dict[total-k]
        sum_dict[total]=sum_dict.get(total,0)+1
    return count

if __name__=='__main__':
    nums = [1,2,3]
    k=3
    print(subarraySum(nums, k))