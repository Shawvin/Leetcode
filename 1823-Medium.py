## 1823. Find the Winner of the Circular Game

def findTheWinner(n: int, k: int):
    l=list(range(1,n+1))
    idx=0
    while len(l)>1:
        if (k+idx-1)>=len(l):
            idx=(k+idx-1)%len(l)
        else:
            idx+=(k-1)
        l.remove(l[idx])
        if idx>=len(l):
            idx=0
        print(l)
    return l[0]

def findTheWinner2(n: int, k: int):
    res=1
    for i in range(2,n+1):
        temp=k%i+1
        res=(res-1+temp-1)%i+1
    return res


if __name__=='__main__':
    n = 5
    k = 2
    print(findTheWinner2(n,k))