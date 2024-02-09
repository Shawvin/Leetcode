## 368. Largest Divisible Subset

## Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
## answer[i] % answer[j] == 0, or
## answer[j] % answer[i] == 0

## dp
def largestDivisibleSubset(nums):
    nums=sorted(nums)
    dp=[[]]*len(nums)
    dp[0]=[nums[0]]
    global_index=0
    global_len=1
    for i in range(1,len(nums)):
        local_index=0
        local_len=1
        for j in range(i):
            if nums[i]%dp[j][-1]==0:
                if local_len<len(dp[j])+1:
                    local_len=len(dp[j])+1
                    local_index=j
        if nums[i]%dp[local_index][-1]==0:
            dp[i]=dp[local_index].copy()
            dp[i].append(nums[i])
        elif local_len>1:
            dp[i]=dp[local_index].copy()
        else:
            dp[i]=[nums[i]]
        if global_len<len(dp[i]):
            global_len=len(dp[i])
            global_index=i
    return dp[global_index]

if __name__=='__main__':
    nums=[5,9,18,54,108,540,90,180,360,720]
    print(largestDivisibleSubset(nums))