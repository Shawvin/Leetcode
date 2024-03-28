## 2958. Length of Longest Subarray With at Most K Frequency

## You are given an integer array nums and an integer k.
## The frequency of an element x is the number of times it occurs in an array.
## An array is called good if the frequency of each element in this array is less than or equal to k.
## Return the length of the longest good subarray of nums.
## A subarray is a contiguous non-empty sequence of elements within an array.

def maxSubarrayLength(nums, k):
    r,l,max_len=0,0,0
    count_dict={}
    while r<len(nums):
        if nums[r] not in count_dict or count_dict[nums[r]]<k:
            count_dict[nums[r]]=count_dict.get(nums[r],0)+1
            max_len=max(max_len,r-l+1)
            r+=1
        else:
            count_dict[nums[l]]-=1
            l+=1
    return max_len

if __name__=='__main__':
    nums=[1,2,3,1,2,3,1,2]
    k=2
    print(maxSubarrayLength(nums, k))