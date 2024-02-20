## 231. Power of Two

## Given an integer n, return true if it is a power of two. Otherwise, return false.
## An integer n is a power of two, if there exists an integer x such that n == 2x.

def isPowerOfTwo(n):
    if n<=0:
        return False
    count=0
    while n:
        if n&1:
            count+=1
        if count>1:
            return False
        n>>=1
    return True

def isPowerOfTwo2(n):
    return n>0 and n&n-1==0

if __name__=='__main__':
    n=16
    print(isPowerOfTwo2(n))