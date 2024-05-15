## 514. Freedom Trail

from collections import defaultdict

def findRotateSteps(ring, key):
    res=[{} for i in range(len(key)+1)]
    char_idx=defaultdict(list)
    n=len(ring)
    for i, char in enumerate(ring):
        char_idx[char].append(i)
    res[0][0]=0
    for i in range(len(key)):
        for idx in char_idx[key[i]]:
            min_count=float('inf')
            for pre_key in res[i]:
                d=min(abs(idx-pre_key), n-abs(idx-pre_key))
                min_count=min(min_count, res[i][pre_key]+d+1)
            res[i+1][idx]=min_count
    return min(res[-1].values())

if __name__=='__main__':
    ring = "godding"
    key = "gd"
    print(findRotateSteps(ring, key))