## 881. Boats to Save People

## You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. 
## Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
## 
## Return the minimum number of boats to carry every given person.

from collections import defaultdict

def numRescueBoats(people, limit):
    p_count=defaultdict(int)
    for p in people:
        p_count[p]+=1
    p_total=len(people)
    w_list=sorted(list(p_count.keys()))
    s=0
    e=len(w_list)-1
    b_count=0
    while p_total>0:
        while p_count[w_list[s]]>0:
            if w_list[s]+w_list[e]>limit:
                b_count+=p_count[w_list[e]]
                p_total-=p_count[w_list[e]]
                p_count[w_list[e]]=0
                e-=1
            else:
                min_count=min(p_count[w_list[s]],p_count[w_list[e]])
                b_count+=min_count
                p_total-=2*min_count
                p_count[w_list[s]]-=min_count
                p_count[w_list[e]]-=min_count
                if p_count[w_list[s]]==0:
                    s+=1
                if p_count[w_list[e]]==0:
                    s-=1
    return b_count

def numRescueBoats2(people, limit):
    people.sort()
    s=0
    e=len(people)-1
    boat=0
    while s<=e:
        if people[s]+people[e]<=limit:
            s+=1
        e-=1
        boat+=1
    return boat

if __name__=='__main__':
    people = [3,5,3,4]
    limit = 5
    print(numRescueBoats(people, limit))