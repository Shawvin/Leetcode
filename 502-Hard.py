## 502. IPO

import heapq

def findMaximizedCapital(k, w, profits, capital):
    profit_capital=zip(profits, capital)
    c_based=[]
    p_based=[]
    for p,c in profit_capital:
        if c<=w:
            heapq.heappush(p_based, (-p,c))
        else:
            heapq.heappush(c_based, (c,p))
    while k>0 and len(p_based)>0:
        p,c=heapq.heappop(p_based)
        w+=(-p)
        k-=1
        while len(c_based)>0 and (c_based[0][0])<=w:
            c,p=heapq.heappop(c_based)
            heapq.heappush(p_based, (-p,c))
    return w

if __name__=='__main__':
    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,1]
    print(findMaximizedCapital(k, w, profits, capital))
