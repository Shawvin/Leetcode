## 1493. Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums) -> int:
        n=len(nums)
        dp=[0]*n
        if nums[-1]==1:
            dp[-1]=1
        else:
            dp[-1]=0
        for i in range(n-2,-1,-1):
            if nums[i]==0:
                dp[i]=0
            else:
                dp[i]=dp[i+1]+1
        pre=0
        res=0
        for j in range(n-1):
            res=max(res, pre+dp[j+1])
            if nums[j]==1:
                pre+=1
            else:
                pre=0
        res=max(res, pre)
        return res
    def longestSubarray2(self, nums) -> int:
        i=0
        j=0
        res=0
        count=0 if nums[0]==1 else 1
        while True:
            if count<=1:
                res=max(res, j-i)
                j+=1
                if j>=len(nums):
                    break
                if nums[j]==0:
                    count+=1
            else:
                if nums[i]==0:
                    count-=1
                i+=1
        return res
    

if __name__=='__main__':
    nums = [0,1,1,1,0,1,1,0,1]
    print(Solution().longestSubarray2(nums))