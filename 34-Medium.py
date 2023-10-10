## 34. Find First and Last Position of Element in Sorted Array
## Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

## If target is not found in the array, return [-1, -1].
def searchRange(nums, target):
    def getIndex(nums, target, left=False):
        lo=0
        hi=len(nums)-1
        idx=-1
        while lo<=hi:
            med=(lo+hi)//2
            if nums[med]==target:
                idx=med
                if left==True:
                    hi=med-1
                else:
                    lo=med+1
            if nums[med]>target:
                hi=med-1
            if nums[med]<target:
                lo=med+1
        return idx
    left_idx=getIndex(nums, target, left=True)
    right_idx=getIndex(nums, target)
    return [left_idx, right_idx]

def searchRange2(nums, target):
    result=[-1,-1]
    if len(nums)==0:
        return result
    for i in range(len(nums)):
        if nums[i]==target:
            result[0]=i
            break
    if result[0]==-1:
        return result
    for i in range(len(nums)-1,-1,-1):
        if nums[i]==target:
            result[1]=i
            break
    return result

if __name__=='__main__':
    nums=[5,7,7,8,8,10]
    target = 8
    print(searchRange(nums, target))