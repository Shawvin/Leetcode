## 1512. Number of Good Pairs
## Given an array of integers nums, return the number of good pairs. A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def numIdenticalPairs(nums):
    num_dict={}
    total=0
    for num in nums:
        num_dict[num]=num_dict.get(num,0)+1
    for num in num_dict:
        count=num_dict[num]
        if count>1:
            total+=count*(count-1)/2
    return int(total)

def numIdenticalPairs2(nums):
    num_dict={}
    total=0
    for num in nums:
        if num in num_dict:
            total+=num_dict[num]
            num_dict[num]+=1
        else:
            num_dict[num]=1
    return total

if __name__=='__main__':
    nums=[1,2,3,1,1,3]
    print(numIdenticalPairs2(nums))