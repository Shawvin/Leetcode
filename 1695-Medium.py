## 1695. Maximum Erasure Value


def maximumUniqueSubarray(nums) -> int:
    pre_map={}
    pre_map[nums[0]]=0
    s=0
    e=0
    res=nums[0]
    cur=nums[0]
    for i in range(1, len(nums)):
        if nums[i] not in pre_map or pre_map[nums[i]]<s:
            cur+=nums[i]
        else:
            cur+=nums[i]                
            for j in range(s, pre_map[nums[i]]+1):
                cur-=nums[j]
            s=pre_map[nums[i]]+1
        pre_map[nums[i]]=i
        res=max(res, cur)
        e=i
    return res

if __name__=='__main__':
    nums = [5,2,1,2,5,2,1,2,5]
    print(maximumUniqueSubarray(nums))