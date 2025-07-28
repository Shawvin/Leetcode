## 2044. Count Number of Maximum Bitwise-OR Subsets

class Solution:
    def countMaxOrSubsets(self, nums) -> int:
        max_or=0
        for num in nums:
            max_or = max_or | num
        self.res = 0  # use instance variable instead of global

        def dfs(i: int, cur_or: int):
            if i == len(nums):
                if cur_or == max_or:
                    self.res += 1
                return
            
            # Exclude nums[i]
            dfs(i + 1, cur_or)
            # Include nums[i]
            dfs(i + 1, cur_or | nums[i])

        dfs(0, 0)
        return self.res
    
    def countMaxOrSubsets2(self, nums) -> int:
        max_or=0
        for num in nums:
            max_or = max_or | num
        self.res = 0  # use instance variable instead of global

        cur_or=0
        def all(i, cur_or):
            if i!=len(nums):
                all(i+1, cur_or)
                cur_or = cur_or | nums[i]
                all(i+1, cur_or)
            else:
                if cur_or==max_or:
                    self.res+=1
                else:
                    return
        all(0, cur_or)
        return self.res

if __name__=='__main__':
     nums = [3,2,1,5]
     print(Solution().countMaxOrSubsets2(nums))