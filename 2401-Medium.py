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

if __name__=='__main__':
    nums = [3,1,5,11,13]
    print(longestNiceSubarray(nums))