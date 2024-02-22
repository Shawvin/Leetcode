## 997. Find the Town Judge

## In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

## If the town judge exists, then:
## The town judge trusts nobody.
## Everybody (except for the town judge) trusts the town judge.
## There is exactly one person that satisfies properties 1 and 2.
## You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. 
## If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
## Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

def findJudge(n,trust):
    if n==1:
        return 1
    trust_count={}
    for a,b in trust:
        if a not in trust_count:
            trust_count[a]=[1,0]
        else:
            trust_count[a][0]+=1
        if b not in trust_count:
            trust_count[b]=[0,1]
        else:
            trust_count[b][1]+=1
    for key in trust_count:
        if trust_count[key][0]==0 and trust_count[key][1]==n-1:
            return key
    return -1

if __name__=='__main__':
    n=3
    trust=[[1,3],[2,3],[3,1]]
    print(findJudge(n,trust))