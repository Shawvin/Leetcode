## 140. Word Break II

def wordBreak(s, wordDict):
    res=[]
    temp=[]
    def backtrack(i, s, wordDict, temp, res):
        if i==len(s):
            res.append(temp.copy())
            return
        for j in range(i, len(s)):
            if s[i:j+1] in wordDict:
                temp.append(s[i:j+1])
                backtrack(j+1, s, wordDict, temp, res)
                temp.pop()
    backtrack(0, s, wordDict, temp, res)
    return [' '.join(x) for x in res]

if __name__=='__main__':
    s = "pineapplepenapple"
    wordDict = ["apple","pen","applepen","pine","pineapple"]
    print(wordBreak(s, wordDict))