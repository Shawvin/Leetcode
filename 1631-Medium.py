## 1631. Path With Minimum Effort

from heapq import heappush,heappop

def minimumEffortPath(heights):
    r_len=len(heights)
    c_len=len(heights[0])
    effort=[[-1]*c_len for i in range(r_len)]
    effort[-1][-1]=0
    h=[]
    heappush(h,(0, r_len-1,c_len-1))
    min_effort=0
    while len(h)>0:
        cur_effort, r,c=heappop(h)
        min_effort=max(min_effort, cur_effort)
        if r==0 and c==0:
            break
        if r>0 and (effort[r-1][c]==-1 or effort[r-1][c]>abs(heights[r][c]-heights[r-1][c])):
            effort[r-1][c]=abs(heights[r][c]-heights[r-1][c])
            heappush(h,(effort[r-1][c], r-1,c))
        if c>0 and (effort[r][c-1]==-1 or effort[r][c-1]>abs(heights[r][c]-heights[r][c-1])):
            effort[r][c-1]=abs(heights[r][c]-heights[r][c-1])
            heappush(h,(effort[r][c-1], r,c-1))
        if r<r_len-1 and (effort[r+1][c]==-1 or effort[r+1][c]>abs(heights[r][c]-heights[r+1][c])):
            effort[r+1][c]=abs(heights[r][c]-heights[r+1][c])
            heappush(h,(effort[r+1][c], r+1,c))
        if c<c_len-1 and (effort[r][c+1]==-1 or effort[r][c+1]>abs(heights[r][c]-heights[r][c+1])):
            effort[r][c+1]=abs(heights[r][c]-heights[r][c+1])
            heappush(h,(effort[r][c+1], r,c+1))
    return min_effort

if __name__=='__main__':
    heights =[[1,10,6,7,9,10,4,9]]
    print(minimumEffortPath(heights))