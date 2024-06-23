## 347. Top K Frequent Elements

## Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

import heapq

def topKFrequent(nums, k):
    l=[]
    res=[]
    map={}
    for num in nums:
        map[num]=map.get(num,0)+1
    for key,v in map.items():
        if len(l)<k:
            heapq.heappush(l,(v,key))
        else:
            heapq.heappush(l,(v,key))
            heapq.heappop(l)
    for v,key in l:
        res.append(key)
    return res

if __name__=='__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums, k))