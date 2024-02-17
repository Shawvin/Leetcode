## 1481. Least Number of Unique Integers after K Removals

## Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

## sort and remove
def findLeastNumOfUniqueInts(arr,k):
    int_dict={}
    for i in arr:
        int_dict[i]=int_dict.get(i,0)+1
    val=list(int_dict.values())
    val=sorted(val)
    while k>0:
        val[0]-=1
        k-=1
        if val[0]==0:
            val.pop(0)
    return len(val)

## sort and remove the lowest frequency
def findLeastNumOfUniqueInts(arr,k):
    int_dict={}
    for i in arr:
        int_dict[i]=int_dict.get(i,0)+1
    val=list(int_dict.values())
    val=sorted(val)
    while k>0:
        freq=val.pop(0)
        if k>=freq:
            k-=freq
        else:
            k=0
            val.append(freq-k)
    return len(val)

if __name__=='__main__':
    arr=[4,3,1,1,3,3,2]
    k=3
    print(findLeastNumOfUniqueInts(arr,k))