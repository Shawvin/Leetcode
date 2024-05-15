## 2226. Maximum Candies Allocated to K Children

def maximumCandies(candies, k):
    total=sum(candies)
    max_candy=total//k
    left=1
    right=max_candy
    res=0
    while left<right:
        count=0
        mid=(left+right)//2
        for candy in candies:
            count+=candy//mid
        if count>=k:
            res=mid
            left=mid+1
        else:
            right=mid-1
    count=0
    for candy in candies:
        count+=candy//left
        if count>=k:
            res=left
    return res

def maximumCandies2(candies, k):
    total=sum(candies)
    max_candy=total//k
    left=0
    right=max_candy
    while left<right:
        count=0
        mid=(left+right+1)//2
        for candy in candies:
            count+=candy//mid
        if count>=k:
            left=mid
        else:
            right=mid-1
    return left

if __name__=='__main__':
    candies = [1,2,3,4,10]
    k = 5
    print(maximumCandies(candies, k))