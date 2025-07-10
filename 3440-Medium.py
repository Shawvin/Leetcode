## 3440. Reschedule Meetings for Maximum Free Time II

import heapq

def maxFreeTime(eventTime: int,startTime, endTime) -> int:
    n=len(startTime)
    free=[0]*(n+1)
    res=0
    top3=list()
    for i in range(n+1):
        if i-1<0:
            t1=0
        else:
            t1=endTime[i-1]
        if i>=n:
            t2=eventTime
        else:
            t2=startTime[i]
        free[i]=t2-t1
        heapq.heappush(top3, (free[i], i))
        if len(top3)>3:
            heapq.heappop(top3)
    for i in range(n):
        block=endTime[i]-startTime[i]
        res=max(res, free[i]+free[i+1])
        for t,j in top3:
            if t>=block and j!=i and j!=i+1:
                res=max(res, free[i]+free[i+1]+block)
    return res

def maxFreeTime2(eventTime: int,startTime, endTime) -> int:
    n=len(startTime)
    res=0
    top3=list()
    for i in range(n+1):
        if i-1<0:
            t1=0
        else:
            t1=endTime[i-1]
        if i>=n:
            t2=eventTime
        else:
            t2=startTime[i]
        heapq.heappush(top3, (t2-t1, i))
        if len(top3)>3:
            heapq.heappop(top3)
    for i in range(n):
        block=endTime[i]-startTime[i]
        if i-1<0:
            t1=0
        else:
            t1=endTime[i-1]
        if i+1>=n:
            t2=eventTime
        else:
            t2=startTime[i+1]
        res=max(res, t2-t1-block)
        for t,j in top3:
            if t>=block and j!=i and j!=i+1:
                res=max(res, t2-t1)
    return res

if __name__=='__main__':
    eventTime = 34
    startTime = [0,17]
    endTime = [14,19]
    print(maxFreeTime(eventTime, startTime, endTime))