## 2402. Meeting Rooms III

## You are given an integer n. There are n rooms numbered from 0 to n - 1.
## You are given a 2D integer array meetings where meetings[i] = [starti, endi] means 
## that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

import heapq

def mostBooked(n, meetings):
    meeting_count=[0]*n
    meeting_time=[0]*n
    meetings.sort(key=lambda x:x[0])
    for meeting in meetings:
        got_room=False
        min_meeting_room_time=float('inf')
        m_idx=n
        for i in range(n):
            if min_meeting_room_time>meeting_time[i]:
                min_meeting_room_time=meeting_time[i]
                m_idx=i
            if meeting_time[i]<=meeting[0]:
                meeting_time[i]=meeting[1]
                meeting_count[i]+=1
                got_room=True
                break
        if not got_room:
            meeting_time[m_idx]+=(meeting[1]-meeting[0])
            meeting_count[m_idx]+=1
    max_count=0
    max_idx=0
    for i,count in enumerate(meeting_count):
        if count>max_count:
            max_count=count
            max_idx=i
    return max_idx

def mostBooked2(n, meetings):
    meetings.sort(key=lambda x:x[0])
    available=[i for i in range(n)]
    print(available)
    occupied=[] #(endtime,roomNo)
    room_count=[0]*n
    for start,end in meetings:
        while occupied and occupied[0][0]<=start:
            _,room=heapq.heappop(occupied)
            heapq.heappush(available, room)
        if len(available)==0:
            endtime,room=heapq.heappop(occupied)
            end=endtime+(end-start)
            heapq.heappush(available, room)
        room=heapq.heappop(available)
        heapq.heappush(occupied, (end,room))
        room_count[room]+=1
    idx=0
    max_count=0
    for i, count in enumerate(room_count):
        if count>max_count:
            max_count=count
            idx=i
    return idx

if __name__=='__main__':
    n=3
    meetings=[[1,20],[2,10],[3,5],[4,9],[6,8]]
    print(mostBooked2(n,meetings))