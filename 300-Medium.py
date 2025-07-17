## 300. Longest Increasing Subsequence

## Given an integer array nums, return the length of the longest strictly increasing subsequence.

def lengthOfLIS(nums):
    max_len=1
    dp=[1]*len(nums)
    for i in range(1,len(nums)):
        local_max=-10**4-1
        for j in range(i-1,-1,-1):
            if nums[j]<nums[i] and nums[j]>local_max:
                dp[i]=max(dp[j]+1, dp[i])
                local_max=nums[j]
        max_len=max(max_len,dp[i])
    print(dp)
    return max_len

def lengthOfLIS2(nums):
    res=[]
    for num in nums:
        if len(res)<1 or res[-1]<num:
            res.append(num)
        else:
            found=False
            i=0
            j=len(res)-1
            while i<=j:
                mid=(i+j)//2
                if res[mid]>num:
                    j=mid-1
                elif res[mid]<num:
                    i=mid+1
                else:
                    found=True
                    break
            if found:
                res[mid]=num
            else:
                res[i]=num
    return len(res)

if __name__=='__main__':
    nums = [10,9,2,5,3,7,101,18]
    print(lengthOfLIS2(nums))