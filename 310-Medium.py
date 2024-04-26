## 310. Minimum Height Trees

from collections import defaultdict

def findMinHeightTrees(n, edges):
    if n<3:
        return list(range(n))
    tree_h={}
    node_h={}
    graph=defaultdict(list)
    degree={}
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
        degree[a]=degree.get(a,0)+1
        degree[b]=degree.get(b,0)+1
    for i in range(n):
        if degree[i]==1:
            continue
        q=[i]
        node_h[i]=0
        visit=[False]*n
        visit[i]=True
        max_height=0
        while q:
            cur=q.pop(0)
            max_height=max(max_height,node_h[cur])
            for next in graph[cur]:
                if not visit[next]:
                    visit[next]=True
                    node_h[next]=node_h[cur]+1
                    q.append(next)
        tree_h[i]=max_height
    min_height=n
    res=[]
    for key in tree_h:
        if tree_h[key]==min_height:
            res.append(key)
        elif tree_h[key]<min_height:
            res=[key]
            min_height=tree_h[key]
    return res

def findMinHeightTrees2(n, edges):
    res=list(range(n))
    if n<3:
        return res
    graph=defaultdict(list)
    degree={}
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
        degree[a]=degree.get(a,0)+1
        degree[b]=degree.get(b,0)+1
    q=[]
    for i in degree:
        if degree[i]==1:
            q.append(i)
    while len(res)>2:
        leaves_count=len(q)
        for i in range(leaves_count):
            leaf=q.pop(0)
            res.remove(leaf)
            for node in graph[leaf]:
                degree[node]-=1
                if degree[node]==1:
                    q.append(node)
    return res

if __name__=='__main__':
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    print(findMinHeightTrees2(n, edges))