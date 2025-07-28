## 2163. Minimum Difference in Sums After Removal of Elements

import heapq

def minimumDifference(nums) -> int:
    min_heap=[]
    max_heap=[]
    n=(len(nums)+1)//3
    temp=0
    record=[0 for i in range(n+1)]
    for i in range(n):
        heapq.heappush(min_heap, -nums[i])
        temp+=nums[i]
    record[0]=temp
    for i in range(n,2*n):
        heapq.heappush(min_heap, -nums[i])
        temp+=nums[i]
        out=heapq.heappop(min_heap)
        temp+=out
        record[i-n+1]=temp
    temp2=0
    res=float('inf')
    for i in range(3*n-1,2*n-1,-1):
        heapq.heappush(max_heap, nums[i])
        temp2+=nums[i]
    res=min(res, record[n]-temp2)
    for i in range(2*n-1,n-1,-1):
        heapq.heappush(max_heap, nums[i])
        temp2+=nums[i]
        out=heapq.heappop(max_heap)
        temp2-=out
        res=min(res, record[i-n]-temp2)
    return res


if __name__=='__main__':
    nums=[7,9,5,8,1,3]

    print(minimumDifference(nums))