## 2368. Reachable Nodes With Restrictions

from collections import defaultdict

def reachableNodes(n, edges, restricted):
    count=1
    q=[]
    q.append(0)
    visit={}
    visit[0]=True
    graph=defaultdict(list)
    restricted=set(restricted)
    for a,b in edges:
        if a not in restricted and b not in restricted:
            graph[a].append(b)
            graph[b].append(a)
    while q:
        cur=q.pop(0)
        for node in graph[cur]:
            if node not in visit:
                visit[node]=True
                count+=1
                q.append(node)
    return count

if __name__=='__main__':
    n = 7
    edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
    restricted = [4,5]
    print(reachableNodes(n, edges, restricted))