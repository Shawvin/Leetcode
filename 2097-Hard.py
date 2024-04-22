## 2097. Valid Arrangement of Pairs

## You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid 
## if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.

## Return any valid arrangement of pairs.
from collections import defaultdict 

def validArrangement(pairs):
    n=len(pairs)
    adj={}
    in_out={}
    for pair in pairs:
        if pair[0] in adj:
            adj[pair[0]].append(pair)
        else:
            adj[pair[0]]=[pair]
        in_out[pair[0]]=in_out.get(pair[0],0)+1
        in_out[pair[1]]=in_out.get(pair[1],0)-1
    path=[]
    circuit=[]
    for key in in_out:
            if in_out[key]==1:
                pair=adj[key].pop()
                pairs.remove(pair)
                n-=1
                path.append(pair)
    while n>0:
        if not len(path):
            pair=pairs.pop(0)
            adj[pair[0]].remove(pair)
            n-=1
            path.append(pair)
        elif path[-1][1] not in adj or not len(adj[path[-1][1]]):
            circuit.append(path.pop())
        else:
            pair=adj[path[-1][1]].pop()
            pairs.remove(pair)
            n-=1
            path.append(pair)
    while path:
        circuit.append(path.pop())
    return circuit[::-1]

def validArrangement2(pairs):
    adj=defaultdict(list)
    in_out={}
    for pair in pairs:
        adj[pair[0]].append(pair[1])          
        in_out[pair[0]]=in_out.get(pair[0],0)+1
        in_out[pair[1]]=in_out.get(pair[1],0)-1
    x=pairs[0][0]
    for key in in_out:
        if in_out[key]==1:
            x=key
    path=[x]
    ans=[]
    while path:
        while adj[path[-1]]:
            path.append(adj[path[-1]].pop())
        ans.append(path.pop())
    ans=ans[::-1]
    return [[ans[i], ans[i+1]] for i in range(len(ans)-1)]

if __name__=='__main__':
    pairs = [[5,13],[10,6],[11,3],[15,19],[16,19],[1,10],[19,11],[4,16],[19,9],[5,11],[5,6],[13,5],[13,9],[9,15],[11,16],[6,9],[9,13],[3,1],[16,5],[6,5]]
    print(validArrangement2(pairs))