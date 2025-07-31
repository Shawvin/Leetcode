## 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        map={}
        start=0
        for i,ch in enumerate(s):
            if ch in map and map[ch]>=start:
                start=map[ch]+1
            res=max(res,i-start+1)
            map[ch]=i
        return res
    
if __name__=='__main__':
    s = "tmmzuxt"
    print(Solution().lengthOfLongestSubstring(s))