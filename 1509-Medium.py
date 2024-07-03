## 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

import heapq

def minDifference(nums):
    def minDifferenceTimes(nums,k):
        if k==0:
            return nums[-1]-nums[0]
        else:
            return min(minDifferenceTimes(nums[1:],k-1), minDifferenceTimes(nums[:-1],k-1))
    
    if len(nums)<=4:
        return 0
    nums.sort()
    return minDifferenceTimes(nums, 3)

def minDifference2(nums):
    if len(nums)<=4:
        return 0
    nums.sort()
    n=len(nums)
    res=nums[-1]-nums[0]
    for i in range(4):
        res=min(res, nums[n-4+i]-nums[i])
    return res

def minDifference3(nums):
    if len(nums)<=4:
        return 0
    min_heap=[]
    max_heap=[]
    for num in nums:
        if len(max_heap)<4:
            heapq.heappush(max_heap, num)
        elif num>max_heap[0]:
            heapq.heappush(max_heap, num)
            heapq.heappop(max_heap)
        if len(min_heap)<4:
            heapq.heappush(min_heap, -num)
        elif (-num)>min_heap[0]:
            heapq.heappush(min_heap, -num)
            heapq.heappop(min_heap)
    res=max_heap[0]+min_heap[3]
    print(min_heap)
    print(max_heap)
    min_heap.sort()
    max_heap.sort()
    print(min_heap)
    print(max_heap)
    for i in range(1,4):
        res=min(res, max_heap[i]+min_heap[3-i])
    return res

if __name__=='__main__':
    nums = [1,5,0,10,14]
    print(minDifference3(nums))