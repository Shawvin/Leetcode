## 392. Is Subsequence

## Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

def isSubsequence(s, t):
    if len(s)==1:
        return s in t
    elif s[0] in t:
        return isSubsequence(s[1:], t[(t.index(s[0])+1):])
    else:
        return False

def isSubsequence2(s, t):
    temp=[True]*(len(t)+1)
    result=[False]*(len(t)+1)
    for i in range(len(s)):
        for j in range(len(t)):
            if t[j]==s[i] and temp[j]==True:
                result[j+1]=True
                while j<len(t):
                    result[j+1]=True
                    j+=1
                break
            result[j+1]=False
        temp=result
        print(temp)
        result=[False]*(len(t)+1)
    return temp[-1]
    

if __name__=='__main__':
     s='abc'
     t='ahbgdc'
     print(isSubsequence2(s,t))