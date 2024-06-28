## 2285. Maximum Total Importance of Roads

from collections import Counter
import functools

def maximumImportance(n, roads):
    node=[0]*n
    for u,v in roads:
        node[u]+=1
        node[v]+=1
    node.sort()
    res=0
    for i,count in enumerate(node):
        res+=(i+1)*count
    return res

def maximumImportance2(n, roads):
    return functools.reduce(lambda x, y: x+y,map(lambda a: (-a[0])*a[1], enumerate(sorted(Counter([x for road in roads for x in road]).values(),reverse=True), start=-n)))

if __name__=='__main__':
    n = 5
    roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
    print(maximumImportance(n, roads))
    print(maximumImportance2(n, roads))