## 2997. Minimum Number of Operations to Make Array XOR Equal to K

def minOperations(nums,k):
    init=0
    for num in nums:
        init ^= num
    count=0
    while init or k:
        if (init%2)!=(k%2):
            count+=1
        init>=1
        k>=1
    return count

if __name__=='__main__':
    nums = [2,1,3,4]
    k = 1
    print(minOperations(nums,k))