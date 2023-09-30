## 456. 132 Pattern

## Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
## Return true if there is a 132 pattern in nums, otherwise, return false.

def find132pattern(nums):
    stack, third=[], float('-inf')

    for num in reversed(nums):
        if num<third:
            return True
        while stack and stack[-1]<num:
            third=stack.pop()
        stack.append(num)
    return False
        

if __name__=='__main__':
     nums=[1,0,1,-4,-3]
     print(find132pattern(nums))