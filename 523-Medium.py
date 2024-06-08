## 523. Continuous Subarray Sum

def checkSubarraySum(nums, k):
    map={}
    map[0]=-1
    cum_sum=0
    for i,num in enumerate(nums):
        cum_sum+=num
        remainder=cum_sum%k
        if remainder in map:
            if (i-map[remainder])>1:
                return True
        else:
            map[remainder]=i
    return False

if __name__=='__main__':
    nums = [0,0]
    k = 1
    print(checkSubarraySum(nums, k))