## 1751. Maximum Number of Events That Can Be Attended II

import heapq

def maxValue(events, k: int) -> int:
    n=max([e[1] for e in events])
    record=[list() for i in range(n+1)]
    events.sort(key=lambda x: x[1])
    print(events)
    j=0
    record[0]=[]
    for i in range(1,n+1):
        while j<len(events) and events[j][1]==i:
            s=events[j][0]
            temp=record[s-1].copy()
            heapq.heappush(temp,events[j][2])
            if len(temp)>k:
                heapq.heappop(temp)
            if sum(temp)>sum(record[i]):
                record[i]=temp
            j+=1
        if sum(record[i-1])>sum(record[i]):
            record[i]=record[i-1]
        print(i)
        print(record[i])
    return sum(record[-1])

if __name__=='__main__':
    events = [[11,17,56],[24,40,53],[5,62,67],[66,69,84],[56,89,15]]
    k = 2
    print(maxValue(events, k))