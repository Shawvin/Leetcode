## 1608. Special Array With X Elements Greater Than or Equal X

def specialArray(nums):
    n=len(nums)
    nums.sort()
    pre=-1
    for i in range(len(nums)):
        cur=nums[i]
        if cur==n-i:
            if cur!=pre:
                return cur
            else:
                return -1
        elif cur<n-i:
            pre=cur
            continue
        else:
            if n-i>pre:
                return n-i
            else:
                return -1
    return -1
    
if __name__=='__main__':
    nums = [0,5,0,1,8,3,0,1]
    print(specialArray(nums))