## 1458. Max Dot Product of Two Subsequences

## Given two arrays nums1 and nums2.
## Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

def maxDotProduct(nums1, nums2):
    result=[[0]*len(nums1) for _ in range(len(nums2))]
    result[0][0]=nums1[0]*nums2[0]
    for i in range(1,len(nums1)):
        result[0][i]=max(result[0][i-1], nums2[0]*nums1[i])
    for j in range(1, len(nums2)):
        result[j][0]=max(result[j-1][0], nums1[0]*nums2[j])
    for i in range(1, len(nums2)):
        for j in range(1, len(nums1)):
            result[i][j]=max(result[i-1][j], result[i][j-1], result[i-1][j-1]+nums2[i]*nums1[j], nums2[i]*nums1[j])
    print(result)
    print(result[7][6])
    return result[-1][-1]

if __name__=='__main__':
    nums1 = [-3,-8,3,-10,1,3,9]
    nums2 = [9,2,3,7,-9,1,-8,5,-1,-1]
    print(maxDotProduct(nums1, nums2))