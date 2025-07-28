## 1186. Maximum Subarray Sum with One Deletion

def maximumSum(arr) -> int:
    l=arr.copy()
    r=arr.copy()
    res=sum(arr)
    n=len(arr)
    if n==1:
        return res
    for i in range(1, len(arr)):
        l[i]=max(l[i], l[i-1]+l[i])
    for i in range(len(arr)-2,-1,-1):
        r[i]=max(r[i], r[i+1]+r[i])
    for j in range(1,len(arr)-1):
        res=max(res, l[j]+r[j+1],l[j-1]+r[j],l[j-1]+r[j+1])
    res=max(res,l[0]+r[1],r[0],r[1])
    res=max(res,l[n-1], l[n-2]+r[n-1], l[n-2])
    return res

if __name__=='__main__':
    arr = [1,-2,-2,3]
    print(maximumSum(arr))