## 2348. Number of Zero-Filled Subarrays

class Solution:
    def zeroFilledSubarray(self, nums) -> int:
        res=0
        n=len(nums)
        start=-1
        for i in range(n):
            if nums[i]==0:
                if start==-1:
                    start=i
            else:
                if start!=-1:
                    temp=(i-start+1)*(i-start)//2
                    res+=temp
                    start=-1
        if start!=-1:
            temp=(n-start+1)*(n-start)//2
            res+=temp
        return res
    
if __name__=='__main__':
    nums =[0,0,0,2,0,0]
    print(Solution().zeroFilledSubarray(nums))