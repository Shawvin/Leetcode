## 238. Product of Array Except Self

## Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
## The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
## You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):
    post={}
    n=len(nums)
    prod=1
    res=[]
    for i in range(n-1,-1,-1):
        prod*=nums[i]
        post[i]=prod
    prod=1
    for i in range(n):
        res.append(prod*post.get(i+1,1))
        prod*=nums[i]
    return res

def productExceptSelf2(nums):
    n=len(nums)
    res=[1]*n
    for i in range(1,n):
        res[i]=res[i-1]*nums[i-1]
    suf_prod=1
    for i in range(n-1,-1,-1):
        res[i]*=suf_prod
        suf_prod*=nums[i]
    return res

if __name__=='__main__':
    nums = [-1,1,0,-3,3]
    print(productExceptSelf(nums))