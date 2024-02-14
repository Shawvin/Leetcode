## 2002. Maximum Product of the Length of Two Palindromic Subsequences

## Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. 
## The two subsequences are disjoint if they do not both pick a character at the same index.
## Return the maximum possible product of the lengths of the two palindromic subsequences.

## A subsequence is a string that can be derived from another string by deleting some or no characters 
## without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.

# enumerate all subsequence
def maxProduct(s):
    n=len(s)
    seq_dict={}
    for i in range(1,(1<<n)-1):
        seq=''
        for j in range(n-1,-1,-1):
            if i&(1<<j):
                seq+=s[j]
        if seq==seq[::-1]:
            seq_dict[i]=len(seq)
    result=0
    for key1 in seq_dict:
        for key2 in seq_dict:
            if key1&key2==0:
                result=max(result, seq_dict[key1]*seq_dict[key2])
    return result

if __name__=='__main__':
    s="leetcodecom"
    print(maxProduct(s))