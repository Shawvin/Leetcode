## 139. Word Break

def wordBreak(s, wordDict):
    def backtrack(i, s, wordDict):
        if i==len(s):
            return True
        res=False
        for j in range(i, len(s)):
            if s[i:j+1] in wordDict:
                res=backtrack(j+1, s, wordDict)
                if res:
                    return res
        return False
    
    return backtrack(0, s, wordDict)

def wordBreak2(s, wordDict):
    dp=[False]*(len(s)+1)
    dp[0]=True
    i=0
    while i<len(s):
        for j in range(i, len(s)):
            if s[i:j+1] in wordDict:
                dp[j+1]=max(dp[i], dp[j+1])
        i+=1
    return dp[-1]

if __name__=='__main__':
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(wordBreak2(s, wordDict))
