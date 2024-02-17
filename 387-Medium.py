## 387. First Unique Character in a String

##Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

## dictionary
def firstUniqChar(s):
    c_dict={}
    for i in range(len(s)):
        if s[i] not in c_dict:
            c_dict[s[i]]=[1,i]
        else:
            c_dict[s[i]][0]+=1
    idx=len(s)
    for char in c_dict:
        if c_dict[char][0]==1:
            idx=min(idx,c_dict[char][1])
    if idx==len(s):
        return -1
    else:
        return idx
    
def firstUniqChar2(s):    
    c_dict={}
    for i in range(len(s)):
        if s[i] in c_dict.keys():
            c_dict[s[i]]=len(s)
        else:
            c_dict[s[i]]=i
    idx=len(s)
    for key in c_dict:
        idx=min(idx, c_dict[key])
    return idx if idx<len(s) else -1

if __name__=='__main__':
    s='leetcode'
    print(firstUniqChar(s))