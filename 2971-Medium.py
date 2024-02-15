## 2971. Find Polygon With the Largest Perimeter

## You are given an array of positive integers nums of length n.
## A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.
## Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, 
## then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

## dynamic plan
def largestPerimeter(nums):
    total=sum(nums)
    nums.sort(reverse=True)
    n=len(nums)
    for i in range(n-2):
        if nums[i]<total-nums[i]:
            return total
        else:
            total-=nums[i]
    return -1

if __name__=='__main__':
    nums=[1,12,1,2,5,50,3]
    print(largestPerimeter(nums))