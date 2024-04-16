## 11. Container With Most Water

def maxArea(height):
    max_water=0
    l=0
    r=len(height)-1
    max_l=height[0]
    max_r=height[-1]
    while l<=r:
        max_l=max(max_l, height[l])
        max_r=max(max_r, height[r])
        max_water=max(min(max_l, max_r)*(r-l), max_water)
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return max_water

if __name__=='__main__':
    height=[1,8,6,2,5,4,8,3,7]
    print(maxArea(height))