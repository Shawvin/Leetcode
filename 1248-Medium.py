## 1248. Count Number of Nice Subarrays

## Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
## Return the number of nice sub-arrays.

def numberOfSubarrays(nums, k):
    idxs=[-1]
    for i, num in enumerate(nums):
        if num%2==1:
            idxs.append(i)
    idxs.append(len(nums))
    i=1
    j=k
    res=0
    while j<len(idxs)-1:
        res+=(idxs[i]-idxs[i-1])*(idxs[j+1]-idxs[j])
        j+=1
        i+=1
    return res

def numberOfSubarrays2(nums, k):
    idxs=[-1]
    res=0
    count=0
    j=1
    for i, num in enumerate(nums):
        if num%2==1:
            idxs.append(i)
            if len(idxs)>k:
                count=idxs[j]-idxs[j-1]
                j+=1
        res+=count
    return res

if __name__=='__main__':
    nums = [1,1,2,1,1]
    k = 3
    print(numberOfSubarrays(nums, k))