## 2441. Largest Positive Integer That Exists With Its Negative

def findMaxK(nums):
    nums.sort()
    s=0
    e=len(nums)-1
    while s<e and nums[s]<0:
        if abs(nums[s])==nums[e]:
            return nums[e]
        elif abs(nums[s])>nums[e]:
            s+=1
        else:
            e-=1
    return -1

if __name__=='__main__':
    nums = [-1,2,-3,3]
    print(findMaxK(nums))