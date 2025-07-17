## 3201. Find the Maximum Length of Valid Subsequence I

def maximumLength(nums) -> int:
    n=len(nums)
    odd=0
    even=0
    pre_odd_idx=-2
    pre_even_idx=-2
    res=0
    for i in range(n):
        if nums[i]%2==0:
            even+=1
            if i-pre_even_idx>1:
                res+=1
            pre_even_idx=i
        if nums[i]%2==1:
            odd+=1
            if i-pre_odd_idx>1:
                res+=1
            pre_odd_idx=i
    return max(res, odd, even)

if __name__=='__main__':
    nums = [1,2,1,1,2,1,2]
    print(maximumLength(nums))