## 1615. Maximal Network Rank

'''
There is an infrastructure of n cities with some number of roads connecting these cities. 
Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.
The network rank of two different cities is defined as the total number of directly connected roads to either city. 
If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.
Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
'''

def maximalNetworkRank(n, roads):
    city_rank=[0]*n
    network_ranks=dict()
    for road in roads:
        city_rank[road[0]]+=1
        city_rank[road[1]]+=1
        network_ranks[(road[0],road[1])]=-1
        network_ranks[(road[1],road[0])]=-1
    for i in range(n):
        for j in range(i+1,n):
            network_ranks[(i,j)]=city_rank[i]+city_rank[j]+network_ranks.get((i,j),0)
            network_ranks[(j,i)]=city_rank[i]+city_rank[j]+network_ranks.get((j,i),0)
    print(network_ranks)
    return max(network_ranks.values())

if __name__=='__main__':
    roads = [[1,0]]
    n=2
    print(maximalNetworkRank(n, roads))