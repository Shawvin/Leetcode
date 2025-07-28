# 3487. Maximum Unique Subarray Sum After Deletion

def maxSum(nums) -> int:
    res=set()
    max_num=nums[0]
    for num in nums:
        if num>max_num:
            max_num=num
        if num>0:
            res.add(num)
    return sum(res) if max_num>0 else max_num

if __name__=='__main__':
    nums = [1,2,3,4,5]
    print(maxSum(nums))