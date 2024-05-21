## 78. Subsets

## Given an integer array nums of unique elements, return all possible 
## subsets (the power set).

## The solution set must not contain duplicate subsets. Return the solution in any order.

def subsets(nums):
    def helper(subnums):
        if len(subnums)==1:
            return [list(),subnums]
        else:
            temp=helper(subnums[:-1])
            return temp+[x+[subnums[-1]] for x in temp]
    
    return helper(nums)

def subsets2(nums):
    res=[]
    temp=[]
    def backtrack(i, temp, nums):
        if i==len(nums):
            res.append(temp.copy())
            return
        temp.append(nums[i])
        backtrack(i+1,temp,nums)
        temp.pop()
        backtrack(i+1,temp,nums)
        
    backtrack(0, temp, nums)
    return res

if __name__=='__main__':
    nums = [1,2,3]
    print(subsets(nums))