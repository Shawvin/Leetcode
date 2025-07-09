## 2008. Maximum Earnings From Taxi

# For each passenger i you pick up, you earn endi - starti + tipi dollars. You may only drive at most one passenger at a time.
# Given n and rides, return the maximum number of dollars you can earn by picking up the passengers optimally.

def maxTaxiEarnings(n: int, rides):
    rides.sort(key=lambda x: (x[1], x[0]))
    res=[0]*(n+1)
    loc_max=0
    for i in range(1,n+1):
        while len(rides)>0 and rides[0][1]==i:
            s,e,t=rides.pop(0)
            loc_max=max(loc_max, res[s]+e-s+t)
        res[i]=loc_max
    return res[-1]

if __name__=='__main__':
    n=20
    rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
    print(maxTaxiEarnings(n, rides))