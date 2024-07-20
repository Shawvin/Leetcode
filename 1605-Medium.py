## 1605. Find Valid Matrix Given Row and Column Sums

import heapq

def restoreMatrix(rowSum, colSum):
    r=[]
    c=[]
    res=[[0]*len(colSum) for i in range(len(rowSum))]
    for i,rs in enumerate(rowSum):
        heapq.heappush(r,(rs,i))
    for i,cs in enumerate(colSum):
        heapq.heappush(c,(cs,i))
    while len(r)>0 or len(c)>0:
        rs,i=heapq.heappop(r)
        cs,j=heapq.heappop(c)
        if rs>=cs:
            res[i][j]=cs
            rs-=cs
            if rs>0:
                heapq.heappush(r,(rs,i))
        else:
            res[i][j]=rs
            cs-=rs
            if cs>0:
                heapq.heappush(c,(cs,j))
    return res

def restoreMatrix2(rowSum, colSum):
    res=[[0]*len(colSum) for i in range(len(rowSum))]
    i,j=0,0
    while i<len(rowSum) and j<len(colSum):
        val=min(rowSum[i], colSum[j])
        res[i][j]=val
        rowSum[i]-=val
        colSum[j]-=val
        if rowSum[i]==0:
            i+=1
        if colSum[j]==0:
            j+=1
    return res


if __name__=='__main__':
    rowSum = [5,7,10]
    colSum = [8,6,8]
    print(restoreMatrix(rowSum, colSum))