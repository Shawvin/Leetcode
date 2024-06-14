## 945. Minimum Increment to Make Array Unique

def minIncrementForUnique(nums):
    nums.sort()
    local_max=nums[0]
    res=0
    for num in nums[1:]:
        local_max=max(local_max+1,num)
        res+=(local_max-num)
    return res

if __name__=='__main__':
    nums = [3,2,1,2,1,7]
    print(minIncrementForUnique(nums))