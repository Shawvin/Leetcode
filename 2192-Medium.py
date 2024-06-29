## 2192. All Ancestors of a Node in a Directed Acyclic Graph

from collections import defaultdict

def getAncestors(n, edges):
    res=[set() for i in range(n)]
    map=defaultdict(list)
    count=[0]*n
    for u,v in edges:
        map[u].append(v)
        count[v]+=1
    temp=[]
    for i in range(n):
        if count[i]==0:
            temp.append(i)
    while len(temp)>0:
        cur=temp.pop(0)
        for c in map[cur]:
            count[c]-=1
            res[c].add(cur)
            res[c].update(res[cur])
            if count[c]==0:
                temp.append(c)
    return [list(sorted(s)) for s in res]

if __name__=='__main__':
    n = 5
    edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    print(getAncestors(n, edges))