## 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit


def longestSubarray(nums, limit):
    l=[nums[0]]
    h=[nums[0]]
    max_len=1
    j=0
    for i in range(1,len(nums)):
        while len(l)>0 and l[-1]>nums[i]:
            l.pop()
        l.append(nums[i])
        while len(h)>0 and h[-1]<nums[i]:
            h.pop()
        h.append(nums[i])
        while h[0]-l[0]>limit:
            if nums[j]==h[0]:
                h.pop(0)
            if nums[j]==l[0]:
                l.pop(0)
            j+=1
        max_len=max(max_len, i-j+1)
    return max_len

if __name__=='__main__':
    nums = [10,1,2,4,7,2]
    limit = 5 
    print(longestSubarray(nums, limit))