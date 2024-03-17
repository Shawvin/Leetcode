## 57. Insert Interval

## You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval 
## and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
## Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals 
## (merge overlapping intervals if necessary).

## Return intervals after the insertion.

def insert(intervals, newInterval):
    res=[]
    inserted=False
    for s,e in intervals:
        if s>newInterval[1]:
            if not inserted:
                res.append(newInterval)
                inserted=True
            res.append([s,e])
        elif e<newInterval[0]:
            res.append([s,e])
        else:
            newInterval[0]=min(s,newInterval[0])
            newInterval[1]=max(e,newInterval[1])
    if not inserted:
        res.append(newInterval)
    return res

if __name__=='__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(insert(intervals, newInterval))
