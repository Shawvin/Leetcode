## 1442. Count Triplets That Can Form Two Arrays of Equal XOR

def countTriplets(arr):
    dp=[0]*(len(arr)+1)
    pre=[dict() for i in range(len(arr))]
    count=0
    for i in range(len(arr)):
        dp[i+1]=dp[i]^arr[i]
        temp=dp[i+1]
        pre[i][temp]=pre[i].get(temp,0)+1
        for j in range(i):
            temp^=arr[j]
            pre[i][temp]=pre[i].get(temp,0)+1
            count+=pre[j].get(temp,0)
    return count

def countTriplets2(arr):
    dp=[0]*(len(arr)+1)
    count=0
    for i in range(len(arr)):
        dp[i+1]=dp[i]^arr[i]
        temp=dp[i+1]
        if temp==0:
            count+=i
        for j in range(i):
            temp^=arr[j]
            if temp==0:
                count+=(i-j-1)
    return count
    
if __name__=='__main__':
    arr = [2,3,1,6,7]
    print(countTriplets(arr))