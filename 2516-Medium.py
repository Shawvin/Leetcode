## 2516. Take K of Each Character From Left and Right

## You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, 
## you may take either the leftmost character of s, or the rightmost character of s.
 
## Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

def takeCharacters(s,k):
    if k==0:
        return 0
    char_dict={}
    for char in s:
        char_dict[char]=char_dict.get(char,0)+1
    char_a=char_dict.get('a',0)-k
    char_b=char_dict.get('b',0)-k
    char_c=char_dict.get('c',0)-k
    if char_a<0 or char_b<0 or char_c<0:
        return -1
    c_dict={'a':0, 'b':0, 'c':0}
    r=-1
    max_len=0
    for i in range(-1,len(s)):
        if i>=0:
            c_dict[s[i]]-=1
        while c_dict['a']<=char_a and c_dict['b']<=char_b and c_dict['c']<=char_c:
            max_len=max(max_len, r-i)
            r+=1
            if r<len(s):
                c_dict[s[r]]+=1
            else:
                break
        if r>=len(s):
            break
    return len(s)-max_len

def takeCharacters2(s,k):
    if k==0:
        return 0
    char_dict={}
    for char in s:
        char_dict[char]=char_dict.get(char,0)+1
    char_a=char_dict.get('a',0)-k
    char_b=char_dict.get('b',0)-k
    char_c=char_dict.get('c',0)-k
    if char_a<0 or char_b<0 or char_c<0:
        return -1
    c_dict={'a':0, 'b':0, 'c':0}
    left=-1
    max_len=0
    idx=0
    for c in s:
        c_dict[c]+=1
        idx+=1
        while c_dict['a']>char_a or c_dict['b']>char_b or c_dict['c']>char_c:
            left+=1
            c_dict[s[left]]-=1
            idx-=1
        max_len=max(max_len, idx)
    return len(s)-max_len

if __name__=='__main__':
    s="aabaaaacaabc"
    k=2
    print(takeCharacters(s,k))