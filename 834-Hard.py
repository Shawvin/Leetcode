## 834. Sum of Distances in Tree

from collections import defaultdict

def sumOfDistancesInTree(n, edges):
    graph=defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    res=[0]*n
    for i in range(n):
        q=[]
        q.append(i)
        visit=[False]*n
        visit[i]=True
        count=0
        while q:
            count+=1
            for j in range(len(q)):
                cur=q.pop(0)
                for nex in graph[cur]:
                    if not visit[nex]:
                        q.append(nex)
                        res[i]+=count
                        visit[nex]=True
    return res

if __name__=='__main__':
    n = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    print(sumOfDistancesInTree(n, edges))