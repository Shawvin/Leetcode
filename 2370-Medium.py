## 2370. Longest Ideal Subsequence

## You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

## - t is a subsequence of the string s.
## -The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
## Return the length of the longest ideal string.

## A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
## Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

def longestIdealString(s,k):
    dict_char=[0]*26
    max_gl=1
    for i in range(len(s)):
        cur=ord(s[i])-ord('a')
        min_i=max(cur-k,0)
        max_i=min(cur+k,26)
        local_max=max(dict_char[min_i:max_i+1])
        dict_char[cur]=local_max+1
        max_gl=max(max_gl, dict_char[cur])
    return max_gl

if __name__=='__main__':
    s = "acfgbd"
    k = 2
    print(longestIdealString(s,k))