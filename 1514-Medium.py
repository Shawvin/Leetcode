## 1514. Path with Maximum Probability

from collections import defaultdict

def maxProbability(n, edges, succProb, start_node, end_node):
    map=defaultdict(dict)
    temp=[start_node]
    res=[0]*n
    res[start_node]=1
    for i in range(len(succProb)):
        map[edges[i][0]][edges[i][1]]=succProb[i]
        map[edges[i][1]][edges[i][0]]=succProb[i]
    while len(temp)>0:
        cur=temp.pop()
        cur_pro=res[cur]
        for edge in map[cur]:
            if cur_pro*map[cur][edge]>res[edge]:
                temp.append(edge)
                res[edge]=cur_pro*map[cur][edge]
    return res[end_node]

def maxProbability2(n, edges, succProb, start_node, end_node):
    map=defaultdict(dict)
    temp=[(-1,start_node)]
    res=[0]*n
    res[start_node]=1
    for i in range(len(succProb)):
        map[edges[i][0]][edges[i][1]]=succProb[i]
        map[edges[i][1]][edges[i][0]]=succProb[i]
    while len(temp)>0:
        cur_pro,cur=heapq.heappop(temp)
        cur_pro=-cur_pro
        if cur==end_node:
            return cur_pro
        for edge in map[cur]:
            if cur_pro*map[cur][edge]>res[edge]:
                heapq.heappush(temp, (-cur_pro*map[cur][edge], edge))
                res[edge]=cur_pro*map[cur][edge]
    return 0

if __name__=='__main__':
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start_node = 0
    end_node = 2
    print(maxProbability(n, edges, succProb, start_node, end_node))