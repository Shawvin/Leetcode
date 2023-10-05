## 229. Majority Element II

## Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

## Boyer-Moore Majority Voting
def majorityElement(nums):
    candidate1, candidate2=None,None
    count1,count2=0,0
    result=[]
    for num in nums:
        if count1==0 and num!=candidate2:
            candidate1=num
            count1=1
            continue
        if count2==0 and num!=candidate1:
            candidate2=num
            count2=1
            continue
        if num==candidate1:
            count1+=1
        elif num==candidate2:
            count2+=1
        else:
            count1-=1
            count2-=1
    
    count1,count2=0,0
    for num in nums:
        if num==candidate1:
            count1+=1
        if num==candidate2:
            count2+=1
    if count1>int(len(nums)/3):
        result.append(candidate1)
    if count2>int(len(nums)/3):
        result.append(candidate2)
    return result

if __name__=='__main__':
    nums = [3,2,3]
    print(majorityElement(nums))