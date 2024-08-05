## 2053. Kth Distinct String in an Array

def kthDistinct(arr, k):
    map={}
    res=[]
    for a in arr:
        if a not in map:
            map[a]=1
            res.append(a)
        else:
            map[a]=0
    idx=0
    for t in res:
        if map[t]>0:
            idx+=1
        if idx==k:
            return t
    return ''

def kthDistinct2(arr, k):
    map={}
    res=[]
    for a in arr:
        if a not in map:
            map[a]=1
            res.append(a)
        else:
            if map[a]!=0:
                res.remove(a)
            map[a]=0
    return res[k-1] if len(res)>=k else ''

if __name__=='__main__':
    arr = ["d","b","c","b","c","a"]
    k = 2
    print(kthDistinct(arr, k))