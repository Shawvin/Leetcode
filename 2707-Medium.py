## 2707. Extra Characters in a String

## You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s 
## into one or more non-overlapping substrings such that each substring is present in dictionary. 
## There may be some extra characters in s which are not present in any of the substrings.

def minExtraChar(s, dictionary):
    extra=[0]*(len(s)+1)
    extra[1]=0 if s[0] in dictionary else 1
    for i in range(1,len(s)):
        min_extra=extra[i]+1
        for j in range(i,-1,-1):
            if extra[j]<min_extra and s[j:i+1] in dictionary:
                curr_extra=extra[j]
                min_extra=min(min_extra,curr_extra)
        extra[i+1]=min_extra
    return extra[-1]

if __name__=='__main__':
    s="sayhelloworld"
    dictionary = ["hello","world"]
    print(minExtraChar(s, dictionary))