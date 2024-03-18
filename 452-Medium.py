## 452. Minimum Number of Arrows to Burst Balloons

## There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points 
## where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
## Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst 
## by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
## Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

def findMinArrowShots(points):
    points.sort()
    cur=points[0]
    count=0
    for s,e in points[1:]:
        if s>cur[1]:
            count+=1
            cur=[s,e]
        else:
            cur[0]=max(cur[0],s)
            cur[1]=min(cur[1],e)
    return count+1

def findMinArrowShots2(points):
    points.sort()
    cur_end=points[0][1]
    count=0
    for s,e in points[1:]:
        if s>cur_end:
            count+=1
            cur_end=e
        else:
            cur_end=min(cur_end,e)
    return count+1

if __name__=='__main__':
    points=[[10,16],[2,8],[1,6],[7,12]]
    print(findMinArrowShots(points))