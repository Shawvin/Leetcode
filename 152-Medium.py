## 152. Maximum Product Subarray

## Given an integer array nums, find a subarray that has the largest product, and return the product.
## The test cases are generated so that the answer will fit in a 32-bit integer.

def maxProduct(nums):
    max_prod=nums[0]
    min_prod=nums[0]
    global_max=nums[0]
    for num in nums[1:]:
        old_max_prod=max_prod
        max_prod=max(max_prod*num, min_prod*num, num)
        global_max=max(global_max, max_prod)
        min_prod=min(old_max_prod*num, min_prod*num,num)
    return global_max

if __name__=='__main__':
    nums=[-2,0,-1]
    print(maxProduct(nums))