## 898. Bitwise ORs of Subarrays


class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        ans = set()
        cur = {0}
        for x in arr:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
    
if __name__=='__main__':
    arr = [1,2,4]
    print(Solution().subarrayBitwiseORs(arr))