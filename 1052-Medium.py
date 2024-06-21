## 1052. Grumpy Bookstore Owner

def maxSatisfied(customers, grumpy, minutes):
    res=0
    base=0
    for i in range(len(grumpy)):
        if grumpy[i]==0:
            base+=customers[i]
    j=minutes
    for i in range(minutes):
        if grumpy[i]==1:
            base+=customers[i]
    res=base
    while j<len(grumpy):
        if grumpy[j]==1:
            base+=customers[j]
        if grumpy[j-minutes]==1:
            base-=customers[j-minutes]
        res=max(res, base)
        j+=1
    return res

def maxSatisfied2(customers, grumpy, minutes):
    base=0
    for i in range(len(grumpy)):
        if grumpy[i]==0:
            base+=customers[i]
        elif i<minutes:
            base+=customers[i]
    j=minutes
    res=base
    while j<len(grumpy):
        if grumpy[j]==1:
            base+=customers[j]
        if grumpy[j-minutes]==1:
            base-=customers[j-minutes]
        res=max(res, base)
        j+=1
    return res

if __name__=='__main__':
    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    minutes = 3
    print(maxSatisfied(customers, grumpy, minutes))