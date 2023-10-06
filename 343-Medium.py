## 343. Integer Break

## Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
## Return the maximum product you can get.

def integerBreak(n):
    result=[0]*(n+1)
    result[0]=1
    result[1]=1
    result[2]=1
    if n>2:
        result[3]=2
    for i in range(2,n+1):
        local_max=result[i-1]
        for j in range(2,i//2+1):
            temp=max(j, result[j])*max(i-j, result[i-j])
            if temp>local_max:
                local_max=temp
        result[i]=local_max
        print("{}:{}".format(i, result[i]))
    return result[n]

if __name__=='__main__':
    n=12
    print(integerBreak(n))    