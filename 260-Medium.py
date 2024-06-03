## 260. Single Number III

def singleNumber(nums):
    temp=0
    for num in nums:
        temp^=num
    lowest=temp&(-temp)
    res=[0,0]
    for num in nums:
        if num&lowest==0:
            res[0]^=num
        else:
            res[1]^=num
    return res

if __name__=='__main__':
    nums = [1,2,1,3,2,5]
    print(singleNumber(nums))