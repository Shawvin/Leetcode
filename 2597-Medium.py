## 2597. The Number of Beautiful Subsets

def beautifulSubsets(nums, k):
    res=[]
    path=[]
    def backtrack(i, path, excluded, nums, k):
        if i==len(nums):
            if len(path)>0:
                res.append(path.copy())
            return
        if nums[i] not in excluded:
            path.append(nums[i])
            excluded.append(nums[i]-k)
            excluded.append(nums[i]+k)
            backtrack(i+1, path, excluded, nums, k)
            path.pop()
            excluded.pop()
            excluded.pop()            
            backtrack(i+1, path, excluded, nums, k)
        else:
            backtrack(i+1, path, excluded, nums, k)

    excluded=[]
    backtrack(0, path, excluded, nums, k)
    return len(res)

def beautifulSubsets2(nums, k):
    cnt=0
    path=[]
    def backtrack(i, path, excluded, nums, k, cnt):
        if i==len(nums):
            if len(path)>0:
                cnt+=1
            return cnt
        if nums[i] not in excluded:
            path.append(nums[i])
            excluded.append(nums[i]-k)
            excluded.append(nums[i]+k)
            cnt=backtrack(i+1, path, excluded, nums, k, cnt)
            path.pop()
            excluded.pop()
            excluded.pop()            
        cnt=backtrack(i+1, path, excluded, nums, k, cnt)
        return cnt
    excluded=[]
    return backtrack(0, path, excluded, nums, k, cnt)

if __name__=='__main__':
    nums = [2,4,6]
    k = 2
    print(beautifulSubsets(nums, k))