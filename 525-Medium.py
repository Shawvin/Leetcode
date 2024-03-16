## 525. Contiguous Array

## Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

def findMaxLength(nums):
    count=0
    max_sub=0
    mp={0:-1}
    for i in range(len(nums)):
        if nums[i]==0:
            count+=1
        else:
            count-=1
        if count in mp:
            max_sub=max(max_sub, i-mp[count])
        else:
            mp[count]=i
    return max_sub

if __name__=='__main__':
    nums = [0,1,0]
    print(findMaxLength(nums))