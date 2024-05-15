## 857. Minimum Cost to Hire K Workers

import heapq

def mincostToHireWorkers(quality, wage, k):
    wq=[(wage[i]/quality[i], i) for i in range(len(quality))]
    wq.sort(key=lambda x:x[0])
    total_q=0
    max_wq=0
    max_heap=[]
    for j in range(k):
        total_q+=quality[wq[j][1]]
        max_wq=wq[j][0]
        heapq.heappush(max_heap, -quality[wq[j][1]])
    total_wage=total_q*max_wq
    for j in range(k, len(quality)):
        max_q=-heapq.heappop(max_heap)
        total_q+=(quality[wq[j][1]]-max_q)
        total_wage=min(total_wage, total_q*wq[j][0])
        heapq.heappush(max_heap, -quality[wq[j][1]])
    return total_wage

if __name__=='__main__':
    quality = [10,20,5]
    wage = [70,50,30]
    k=2
    print(mincostToHireWorkers(quality, wage, k))