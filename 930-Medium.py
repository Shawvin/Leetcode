## 930. Binary Subarrays With Sum

## Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
## A subarray is a contiguous part of the array.

def numSubarraysWithSum(nums, goal):
    sum_dict={}
    total=0
    sum_dict[0]=1
    for val in nums:
        total+=val
        sum_dict[total]=sum_dict.get(total,0)+1
    count=0
    for key in sum_dict:
        if goal==0:
            count+=int(sum_dict[key]*(sum_dict[key]-1)/2)
        elif goal+key in sum_dict:
            count+=sum_dict[key]*sum_dict[key+goal]
    return count

def numSubarraysWithSum2(nums, goal):
    sum_dict={}
    sum_dict[0]=1
    total=0
    count=0
    for val in nums:
        total+=val
        if total-goal in sum_dict:
            count+=sum_dict[total-goal]
        sum_dict[total]=sum_dict.get(total,0)+1    
    return count

if __name__=='__main__':
    nums=[1,0,1,0,1]
    goal=2
    print(numSubarraysWithSum(nums, goal))