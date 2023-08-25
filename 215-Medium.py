## 215. Kth Largest Element in an Array

## Given an integer array nums and an integer k, return the kth largest element in the array.
## Note that it is the kth largest element in the sorted order, not the kth distinct element.

def findKthLargest(nums, k):
    index=0
    pivot=nums[-1]
    for i in range(len(nums)):
        if nums[i]>pivot:
            nums[i],nums[index]=nums[index],nums[i]
            index+=1
    if index==k-1:
        return pivot
    elif index>k-1:
        return findKthLargest(nums[0:index], k)
    else:
        nums[index],nums[-1]=nums[-1],nums[index]
        return findKthLargest(nums[index+1:], k-1-index)

if __name__=='__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(findKthLargest(nums, k))