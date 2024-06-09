## 974. Subarray Sums Divisible by K

from collections import defaultdict

def subarraysDivByK(nums, k):
    map=defaultdict(list)
    cur=0
    res=0
    for i,num in enumerate(nums):
        cur+=num
        temp=cur%k
        res+=len(map[temp])
        map[temp].append(i)
        if temp==0:
            res+=1
    return res

if __name__=='__main__':
    nums = [4,5,0,-2,-3,1]
    k = 5
    print(subarraysDivByK(nums, k))