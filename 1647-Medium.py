## 1647. Minimum Deletions to Make Character Frequencies Unique

## A string s is called good if there are no two different characters in s that have the same frequency.
## Given a string s, return the minimum number of characters you need to delete to make s good.

def minDeletions(s):
    freq_dict={}
    for char in s:
        freq_dict[char]=freq_dict.get(char,0)+1
    used_freq=set()
    deletions=0
    for key, freq in freq_dict.items():
        if freq>0 and freq not in used_freq:
            used_freq.add(freq)
            continue
        while (freq in used_freq and freq>0):
            freq-=1
            deletions+=1
        if freq!=0:
            used_freq.add(freq)
    return deletions

if __name__=='__main__':
    s="aaabbbcc"
    print(minDeletions(s))