## 2874. Maximum Value of an Ordered Triplet II

def maximumTripletValue(nums: list[int]) -> int:
    n=len(nums)
    maxl1=[0]*n
    maxl2=[0]*n
    max_val=nums[0]
    for i in range(n):
        max_val=max(max_val, nums[i])
        maxl1[i]=max_val
    max_val=nums[n-1]
    for i in range(n-1,-1,-1):
        max_val=max(max_val, nums[i])
        maxl2[i]=max_val
    
    res=0
    for i in range(1,n-1):
        res=max(res, max(maxl1[i-1]-nums[i],0)*maxl2[i+1])
    return res

if __name__=='__main__':
    nums = [8,6,3,13,2,12,19,5,19,6,10,11,9]
    maximumTripletValue(nums)