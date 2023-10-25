## 779. K-th Symbol in Grammar

## We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, 
## we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
## Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

def kthGrammar(n, k):
        return upperrow(k)
    
def upperrow(k):
    if k==1:
        return 0
    if k%2==0:
        k=(k+1)//2
        return 1-upperrow(k)
    else:
        k=(k+1)//2
        return upperrow(k)
    
if __name__=='__main__':
    n=2
    k=1
    print(kthGrammar(n,k))