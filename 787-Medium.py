## 787. Cheapest Flights Within K Stops

## There are n cities connected by some number of flights. You are given an array flights where 
## flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

## You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
## If there is no such route, return -1.

# BFS
def findCheapestPrice(n, flights, src,dst,k):
    costs=[0]*n #indicate the lowest cost to reach this city from src
    to_city={}
    for f,t,price in flights:
        if f in to_city:
            to_city[f].append((t,price))
        else:
            to_city[f]=[(t,price)]
    st=[]
    st.append((src,0,0)) #current city, current stops, current cost
    while st:
        city, stop, cost=st.pop(0)
        if stop>k or city not in to_city:
            continue
        for t, price in to_city[city]:
            if costs[t]==0 or costs[t]>cost+price:
                costs[t]=cost+price
                st.append((t,stop+1,cost+price))
    if costs[dst]==0:
        return -1
    else:
        return costs[dst]


if __name__=='__main__':
    n=5
    flights=[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
    src=0
    dst=2
    k=2
    print(findCheapestPrice(n, flights, src,dst,k))