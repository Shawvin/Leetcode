## 1915. Number of Wonderful Substrings

from collections import defaultdict
def wonderfulSubstrings(word):
    n=len(word)
    res=0
    for i in range(n):
        count=[0]*10
        q=[]
        for j in range(i,n):
            count[ord(word[j])-ord('a')]+=1
            if count[ord(word[j])-ord('a')]%2==1:
                q.append(word[j])
            else:
                q.remove(word[j])
            if len(q)<=1:
                res+=1
    return res

def wonderfulSubstrings2(word):
    count = defaultdict(int)
    count[0] = 1
    result = 0
    bitmask = 0
    
    for char in word:
        char_index = ord(char) - ord('a')
        bitmask ^= 1 << char_index
        result += count[bitmask]
        for i in range(10):
            result += count[bitmask ^ (1 << i)]
        count[bitmask] += 1
    
    return result

def wonderfulSubstrings3(word):
    n=len(word)
    res=1
    bitmask=[0]*n
    bitmask[0]=1<<(ord(word[0])-ord('a'))
    for i in range(1,n):
        shift=ord(word[i])-ord('a')
        mask=-1-(1<<shift)
        bitmask[i]=(~bitmask[i-1])^mask
        if bitmask[i].bit_count()<=1:
            res+=1
        for j in range(i):
            if (bitmask[i]^bitmask[j]).bit_count()<=1:
                res+=1
    return res

if __name__=='__main__':
    word = "aabb"
    print(wonderfulSubstrings2(word))