## 2540. Minimum Common Value

## Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. 
## If there is no common integer amongst nums1 and nums2, return -1.
## 
## Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

## two pointer
def getCommon(nums1, nums2):
    first=0
    second=0
    while first<len(nums1) and second<len(nums2):
        if nums1[first]==nums2[second]:
            return nums1[first]
        elif nums1[first]>nums2[second]:
            second+=1
        else:
            first+=1
    return -1

if __name__=='__main__':
    nums1=[1,2,3,6]
    nums2=[2,3,4,5]
    print(getCommon(nums1, nums2))