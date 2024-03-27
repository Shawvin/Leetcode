## 1980. Find Unique Binary String

## Given an array of strings nums containing n unique binary strings each of length n, 
## return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

def findDifferentBinaryString(nums):
    l=len(nums)
    res=[-1]*l
    for num in nums:
        n=int(num,2)
        if n<l:
            res[n]=n
    for i in range(l):
        if res[i]<0:
            return str(bin(i))[2:].zfill(l)
    return str(bin(l))[2:].zfill(l)

def findDifferentBinaryString2(nums):
    ans = ""

    index = 0
    for bin_num in nums:
        ans = ans + str(1-int(bin_num[index],10))
        index+=1
    return ans
        
if __name__=='__main__':
    nums=["1111","0111","0000","1000"]
    print(findDifferentBinaryString(nums))