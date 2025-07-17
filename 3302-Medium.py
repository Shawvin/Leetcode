## 3202. Find the Maximum Length of Valid Subsequence II

def maximumLength(nums, k) -> int:
    res=0
    for val in range(k):
        dp=[0 for i in range(k)]
        for num in nums:
            i=num%k
            j=(k+val-(num%k))%k
            dp[i]=dp[j]+1
            res=max(res, dp[i])
    return res

if __name__=='__main__':
    nums = [1,2,3,4,5]
    k = 2
    print(maximumLength(nums, k))