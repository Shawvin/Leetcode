## 2751. Robot Collisions

import heapq
from collections import defaultdict

def survivedRobotsHealths(positions, healths, directions):
    res=[]
    battle=[]
    l=[]
    r=[]
    robots=defaultdict(list)
    for i, p in enumerate(positions):
        robots[p]=[i,healths[i]]
        if directions[i]=='R':
            heapq.heappush(r, p)
        else:
            heapq.heappush(l, p)
    while len(l)>0 and (len(r)>0 or len(battle)>0):
        if len(r)>0 and l[0]>r[0]:
            battle.append(heapq.heappop(r))
        else:
            if len(battle)==0:
                res.append(robots[l[0]])
                heapq.heappop(l)
            while len(battle)>0:
                if robots[battle[-1]][1]<robots[l[0]][1]:
                    robots[l[0]][1]-=1
                    battle.pop()
                    if len(battle)==0:
                        res.append(robots[l[0]])
                        heapq.heappop(l)
                elif robots[battle[-1]][1]==robots[l[0]][1]:
                    battle.pop()
                    heapq.heappop(l)
                    break
                else:
                    robots[battle[-1]][1]-=1
                    heapq.heappop(l)
                    break
    if len(l)>0:
        for p in l:
            res.append(robots[p])
    else:
        for p in battle:
            res.append(robots[p])
        for p in r:
            res.append(robots[p])
    res.sort(key=lambda x:x[0])
    return [x[1] for x in res]

def survivedRobotsHealths2(positions, healths, directions):
    pd=list(zip(positions, directions))
    pd.sort()
    pos_hi=defaultdict(list)
    for i, pos in enumerate(positions):
        pos_hi[pos]=[i,healths[i]]
    st=[]
    for pos, d in pd:
        if len(st)==0 or st[-1][1]==d or st[-1][1]=='L':
            st.append((pos,d))
        else:
            while len(st)!=0 and st[-1][1]=='R':
                if pos_hi[st[-1][0]][1]>pos_hi[pos][1]:
                    pos_hi[st[-1][0]][1]-=1
                    break
                elif pos_hi[st[-1][0]][1]==pos_hi[pos][1]:
                    st.pop()
                    break
                else:
                    pos_hi[pos][1]-=1
                    st.pop()
                    if len(st)==0 or st[-1][1]=='L':
                        st.append((pos,d))
                        break
    return [x[1] for x in sorted([pos_hi[x[0]] for x in st])]

if __name__=='__main__':
    positions = [3,5,2,6]
    healths = [10,10,15,12]
    directions = "RLRL"
    print(survivedRobotsHealths(positions, healths, directions))