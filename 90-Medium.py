## 90. Subsets II

## Given an integer array nums that may contain duplicates, return all possible 
## subsets (the power set).
## 
## The solution set must not contain duplicate subsets. Return the solution in any order.

def subsetsWithDup(nums):
    res=set()
    temp=[]
    nums.sort()
    def backtrack(i, temp, nums):
        if i==len(nums):
            res.add(tuple(temp.copy()))
            return
        temp.append(nums[i])
        backtrack(i+1, temp, nums)
        temp.pop()
        backtrack(i+1, temp, nums)
    
    backtrack(0, temp, nums)
    return [list(x) for x in res]

if __name__=='__main__':
    nums = [4,4,4,1,4]
    print(subsetsWithDup(nums))