## 2615. Sum of Distances

## You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j 
## such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.
## 
## Return the array arr.

def distance(nums):
    arr=[0]*len(nums)
    cnt=[0]*len(nums)
    dict_c={}
    count_c={}
    for i in range(len(nums)):
        if nums[i] in dict_c:
            dict_c[nums[i]]+=i
            count_c[nums[i]]+=1
        else:
            dict_c[nums[i]]=i
            count_c[nums[i]]=1
        arr[i]=-dict_c[nums[i]]
        cnt[i]=count_c[nums[i]]
    for i in range(len(nums)):
        arr[i]=dict_c[nums[i]]+arr[i]+arr[i]+i+(2*cnt[i]-1-count_c[nums[i]])*i
    return arr

if __name__=='__main__':
    nums=[0,5,3]
    print(distance(nums))