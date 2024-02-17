## 1642. Furthest Building You Can Reach

## You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
## You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

## While moving from building i to building i+1 (0-indexed),

## If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
## If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.

import heapq

def furthestBuilding(heights, bricks, ladders):
    ladder_list=[]
    total_jump=0
    ladder_jump=0
    for i in range(1,len(heights)):
        if heights[i]<heights[i-1]:
            continue
        else:
            jump=heights[i]-heights[i-1]
            total_jump+=jump
            if len(ladder_list)<ladders:
                heapq.heappush(ladder_list,jump)
                ladder_jump+=jump
            if len(ladder_list)>0 and len(ladder_list)==ladders:
                min_jump=heapq.heappop(ladder_list)
                if jump>min_jump:
                    heapq.heappush(ladder_list,jump)
                    ladder_jump+=jump
                    ladder_jump-=min_jump
                else:
                    heapq.heappush(ladder_list,min_jump)
            if total_jump-ladder_jump>bricks:
                return i-1
    return len(heights)-1

# heapq queue
def furthestBuilding2(heights, bricks, ladders):
    ladder_list=[]
    for i in range(1,len(heights)):
        if heights[i]<heights[i-1]:
            continue
        else:
            jump=heights[i]-heights[i-1]
            bricks-=jump
            heapq.heappush(ladder_list,-jump)
            if bricks<0:
                bricks-=heapq.heappop(ladder_list)
                ladders-=1
            if ladders<0:
                return i-1
    return len(heights)-1

def furthestBuilding3(heights, bricks, ladders):
    ladder_list=[]
    total_jump=0
    for i in range(1,len(heights)):
        if heights[i]<heights[i-1]:
            continue
        jump=heights[i]-heights[i-1]
        heapq.heappush(ladder_list,jump)
        if len(ladder_list)>ladders:
            min_jump=heapq.heappop(ladder_list)
            total_jump+=min_jump
        if total_jump>bricks:
            return i-1
    return len(heights)-1

if __name__=='__main__':
    heights=[4,12,2,7,3,18,20,3,19]
    bricks=10
    ladders=2
    print(furthestBuilding(heights, bricks, ladders))