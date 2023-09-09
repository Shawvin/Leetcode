# Given an array of distinct integers nums and a target integer target, return the number
# of possible combinations that add up to target.

def combinationSum4(nums, target):
    result=[0]*(target+1)
    result[0]=1
    for i in range(1, target+1):
        for num in nums:
            if i>=num:
                result[i]+=result[i-num]
    return result[-1]

if __name__=='__main__':
    nums=[1,2,3]
    target=4
    print(combinationSum4(nums, target))