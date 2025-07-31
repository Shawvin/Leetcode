## 2401. Longest Nice Subarray

def longestNiceSubarray(nums):
    max_l=1
    s=0
    e=0
    while e<len(nums):
        for j in range(e-1,s-1,-1):
            if nums[j]&nums[e]!=0:
                s=j+1
                break
        max_l=max(max_l,e-s+1)
        e+=1
    return max_l

def longestNiceSubarray2(nums):
    i=0
    cur=nums[0]
    n=len(nums)
    if n==1:
        return 1
    j=1
    res=1
    while j<n:
        if cur & nums[j]==0:
            cur=cur | nums[j]
            j+=1
            res=max(res, j-i)
        else:
            if j-i==1:
                cur=nums[j]
                j+=1
            else:
                cur = cur ^ nums[i]
            i+=1
    return res

if __name__=='__main__':
    nums = [3,1,5,11,13]
    print(longestNiceSubarray(nums))