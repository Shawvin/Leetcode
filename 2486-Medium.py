## 2486. Append Characters to String to Make Subsequence

## You are given two strings s and t consisting of only lowercase English letters.
## Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

def appendCharacters(s,t):
    idx1=0
    idx2=0
    while idx1<len(t):
        while idx2<len(s):
            if t[idx1]==s[idx2]:
                idx1+=1
                idx2+=1
                break
            else:
                idx2+=1
        if idx2==len(s):
            break
    return len(t)-idx1

def appendCharacters2(s,t):
    idx1=0
    idx2=0
    t_len=len(t)
    s_len=len(s)
    while idx1<t_len and idx2<s_len:
        if t[idx1]==s[idx2]:
            idx1+=1
        idx2+=1
    return t_len-idx1


if __name__=='__main__':
    s = "coaching"
    t = "coding"
    print(appendCharacters(s,t))