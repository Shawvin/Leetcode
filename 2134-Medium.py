## 2134. Minimum Swaps to Group All 1's Together II

def minSwaps(nums):
    count=0
    n=len(nums)
    for num in nums:
        if num==1:
            count+=1
    res=0
    for i in range(count):
        if nums[i]==0:
            res+=1
    swap=res
    for i in range(count,n+count):
        if nums[i-count]==0:
            res-=1
        if nums[i%n]==0:
            res+=1
        swap=min(swap,res)
    return swap

if __name__=='__main__':
    nums = [0,1,0,1,1,0,0]
    print(minSwaps(nums))