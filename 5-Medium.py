## 5. Longest Palindromic Substring

## Given a string s, return the longest palindromic substring in s

class Solution:
    def longestPalindrome(self, s: str) -> str:
        count=0
        for i in range(len(s)):
            start=i
            end=i
            while start>=0 and s[start]==s[i]:
                start-=1
            while end<len(s) and s[end]==s[i]:
                end+=1
            while start>=0 and end<len(s):
                if s[start]==s[end]:
                    start-=1
                    end+=1
                else:
                    break
            if end-start-1>count:
                count=end-start-1
                res=s[start+1:end]
        return res
    
if __name__=='__main__':
    s = "tmmzuxt"
    print(Solution().longestPalindrome(s))