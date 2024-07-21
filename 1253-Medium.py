## 1253. Reconstruct a 2-Row Binary Matrix

def reconstructMatrix(upper, lower, colsum):
    res=[[0]*len(colsum) for i in range(2)]
    for i in range(len(colsum)):
        if colsum[i]==2:
            upper-=1
            lower-=1
            res[0][i]=1
            res[1][i]=1
        elif colsum[i]==1:
            if upper>lower:
                upper-=1
                res[0][i]=1
            else:
                lower-=1
                res[1][i]=1
    return res if lower==0 and upper==0 else []

if __name__=='__main__':
    upper = 5
    lower = 5
    colsum = [2,1,2,0,1,0,1,2,0,1]
    print(reconstructMatrix(upper, lower, colsum))