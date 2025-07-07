## 1353. Maximum Number of Events That Can Be Attended

# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
# Return the maximum number of events you can attend.

import heapq

def maxEvents(events):
    events.sort()
    max_day = max(event[1] for event in events)    
    temp=[]  
    res=0
    i=0
    for t in range(1,max_day + 1):
        while len(temp)>0 and temp[0][0]<t:
            heapq.heappop(temp)
        while i<len(events) and events[i][0]<=t:
            heapq.heappush(temp, (events[i][1], events[i][0]))
            i+=1
        if len(temp)>0:
            heapq.heappop(temp)
            res+=1
    return res

if __name__=='__main__':
    events = [[1,2],[2,3],[3,4],[1,2]]
    print(maxEvents(events))