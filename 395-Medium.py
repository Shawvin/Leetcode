## 395. Longest Substring with At Least K Repeating Characters

## Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
## if no such substring exists, return 0.

## divide and conquer
def longestSubstring(s,k):
    char_dict={}
    for char in s:
        char_dict[char]=char_dict.get(char,0)+1
    l,r,max_len=0,0,0
    while r<len(s):
        if char_dict[s[r]]>=k:
            r+=1
        else:
            max_len=max(longestSubstring(s[:r],k), longestSubstring(s[r+1:],k))
            break
    if r==len(s):
        max_len=max(max_len, len(s))
    return max_len

if __name__=='__main__':
    s='ababbc'
    k=2
    print(longestSubstring(s,k))