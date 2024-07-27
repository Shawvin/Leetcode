## 2976. Minimum Cost to Convert String I

from collections import defaultdict

def minimumCost(source, target, original, changed, cost):
    map=defaultdict(list)
    for i in range(len(original)):
        map[original[i]].append((changed[i], cost[i]))
    change_cost={}
    for c in list(map.keys()):
        l=[(c,0)]
        while len(l)>0:
            cur,cst=l.pop(0)
            for d,d_cst in map[cur]:
                key=c+d
                if key not in change_cost or cst+d_cst<change_cost[key]:
                    change_cost[key]=cst+d_cst
                    l.append((d,cst+d_cst))
    res=0
    for s,t in zip(source,target):
        if s==t:
            continue
        key=s+t
        if key not in change_cost:
            return -1
        else:
            res+=change_cost[key]
    return res

if __name__=='__main__':
    source = "abcd"
    target = "acbe"
    original = ["a","b","c","c","e","d"]
    changed = ["b","c","b","e","b","e"]
    cost = [2,5,5,1,2,20]
    print(minimumCost(source, target, original, changed, cost))