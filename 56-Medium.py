## 56. Merge Intervals

## Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
## and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    cur=intervals[0]
    res=[]
    for s,e in intervals[1:]:
        if s>cur[1]:
            res.append(cur)
            cur=[s,e]
        else:
            cur[0]=min(cur[0],s)
            cur[1]=max(cur[1],e)
    res.append(cur)
    return res

if __name__=="__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals))