## 416. Partition Equal Subset Sum

def canPartition(nums: list[int]) -> bool:
    total=0
    for num in nums:
        total+=num
    if total%2==1:
        return False
    target=total//2
    track=[0]*(target+1)
    track[0]=1
    for num in nums:
        for key in range(target-num,-1,-1):
            if track[key+num]!=1:
                track[key+num]=track[key]
        if track[target]==1:
            return True
    return track[target]==1

if __name__=='__main__':
    nums = [14,9,8,4,3,2]
    print(canPartition(nums))
