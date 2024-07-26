## 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

from collections import defaultdict

def findTheCity(n, edges, distanceThreshold):
    min_city=n
    graph=defaultdict(list)
    for f,t,w in edges:
        graph[f].append((t,w))
        graph[t].append((f,w))
    for i in range(n):
        visit=dict()
        visit[i]=0
        l=[i]
        count=1
        while len(l)>0:
            cur=l.pop(0)
            cur_w=visit[cur]
            for city, w in graph[cur]:
                if cur_w+w<=distanceThreshold:
                    if city not in visit:
                        l.append(city)
                        count+=1
                        visit[city]=cur_w+w
                    elif cur_w+w<visit[city]:
                        l.append(city)
                        visit[city]=cur_w+w
            if count>min_city:
                break
        if count<=min_city:
            min_city=count
            res=i
    return res

if __name__=='__main__':
    n = 5
    edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
    distanceThreshold = 2
    print(findTheCity(n, edges, distanceThreshold))