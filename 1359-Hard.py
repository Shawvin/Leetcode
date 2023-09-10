## 1359. Count All Valid Pickup and Delivery Options
## Given n orders, each order consist in pickup and delivery services. 

## Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

## Since the answer may be too large, return it modulo 10^9 + 7.

def countOrders(n):
    result=[0]*(n+1)
    result[0]=1
    result[1]=1
    for i in range(2,n+1):
        result[i]=result[i-1]*i*(2*i-1)
    return result[n]%(10**9+7)

def countOrders2(n):
    result=1
    for i in range(2,n+1):
        result=result*i*(2*i-1)
    return result%(10**9+7)

if __name__=='__main__':
    n=3
    print(countOrders2(n))