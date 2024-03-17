## 2405. Optimal Partition of String

## Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. 
## That is, no letter appears in a single substring more than once.
## Return the minimum number of substrings in such a partition.
## Note that each character should belong to exactly one substring in a partition.

def partitionString(s):
    rec_char={}
    idx=0
    count=0
    for i,char in enumerate(s):
        if char in rec_char and rec_char[char]>=idx:
            count+=1
            idx=i
        rec_char[char]=i
    return count+1

if __name__=='__main__':
    s = "abacaba"
    print(partitionString(s))