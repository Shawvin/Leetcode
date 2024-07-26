## 2191. Sort the Jumbled Numbers

def sortJumbled(mapping, nums):
    strmapping={}
    for i,num in enumerate(mapping):
        strmapping[str(i)]=str(num)
    
    new_nums=[str(x) for x in nums]
    new_nums=[int(''.join(list(map(lambda x: strmapping[x], y)))) for y in new_nums]

    return [nums[i] for i,_ in sorted(enumerate(new_nums),key=lambda x:x[1])]

if __name__=='__main__':
    mapping = [8,9,4,0,2,1,3,5,7,6]
    nums = [991,338,38]
    print(sortJumbled(mapping, nums))