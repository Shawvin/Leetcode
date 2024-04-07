## 2962. Count Subarrays Where Max Element Appears at Least K Times

## You are given an integer array nums and a positive integer k.
## 
## Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
## 
## A subarray is a contiguous sequence of elements within an array.

def countSubarrays(nums,k):
    max_num=nums[0]
    max_idx=[0]
    for i in range(1,len(nums)):
        if nums[i]>max_num:
            max_num=nums[i]
            max_idx=[i]
        elif nums[i]==max_num:
            max_idx.append(i)
    if len(max_idx)<k:
        return 0
    c_idx=len(nums)
    total=0
    cur=0
    j_idx=0
    pre_j=-1
    pre_i=max_idx[k-1]
    for i_idx in range(k-1,len(max_idx)):
        i=max_idx[i_idx]
        total+=(cur*(i-pre_i))
        j=max_idx[j_idx]
        cur+=(j-pre_j)
        pre_j=j
        j_idx+=1
        pre_i=i
    total+=(cur*(c_idx-pre_i))
    return total

if __name__=='__main__':
    nums=[1,3,2,3,3]
    k=2
    print(countSubarrays(nums,k))