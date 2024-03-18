## 435. Non-overlapping Intervals

## Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals 
## you need to remove to make the rest of the intervals non-overlapping.

def eraseOverlapIntervals(intervals):
    intervals.sort()
    cur_end=intervals[0][1]
    count=0
    for s,e in intervals[1:]:
        if s>=cur_end:
            cur_end=e
        else:
            count+=1
            cur_end=min(cur_end,e)
    return count

if __name__=='__main__':
    intervals=[[1,2],[2,3],[3,4],[1,3]]
    print(eraseOverlapIntervals(intervals))