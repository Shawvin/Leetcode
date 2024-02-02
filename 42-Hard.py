## 42. Trapping Rain Water

## Given n non-negative integers representing an elevation map where the width of each bar is 1, 
## compute how much water it can trap after raining.

def trap(height):
    l=len(height)
    if l<3:
        return 0
    left_hi=height[0]
    right_hi=max(height[2:])
    waters=[0]*(l-2)
    for i in range(1,l-1):
        left_hi=max(left_hi,height[i-1])
        if height[i]==right_hi:
            right_hi=max(height[i+1:])
            continue
        else:
            min_hi=min(left_hi,right_hi)
            if min_hi>height[i]:
                waters[i-1]=min_hi-height[i]
    return sum(waters)

def trap2(height):
    l=len(height)
    if l<3:
        return 0
    left_hi=height[0]
    right_hi=[0]*(l)
    right_hi[l-2]=height[l-1]
    for i in range(l-3,0,-1):
        right_hi[i]=max(right_hi[i+1],height[i+1])
    water=0
    for i in range(1,l-1):
        left_hi=max(left_hi,height[i-1])           
        min_hi=min(left_hi,right_hi[i])
        if min_hi>height[i]:
            water+=(min_hi-height[i])
    return water

def trap3(height):
    l=len(height)
    if l<3:
        return 0
    water=0
    left=1
    right=l-2
    left_hi=height[0]
    right_hi=height[l-1]
    while left<=right:
        left_hi=max(left_hi,height[left-1])
        right_hi=max(right_hi,height[right+1])
        if left_hi<right_hi:
            if left_hi>height[left]:
                water+=(left_hi-height[left])
            left+=1
        else:
            if right_hi>height[right]:
                water+=(right_hi-height[right])
            right-=1
    return water

if __name__=='__main__':
    height=[4,2,0,3,2,5]
    print(trap(height))
