## 646. Maximum Length of Pair Chain
## You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
## A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
## Return the length longest chain which can be formed.

def findLongestChain(pairs):
    pairs.sort(key=lambda k:(k[0],k[1]))
    print(pairs)
    result=[1]+[0]*(len(pairs)-1)
    for i in range(len(pairs)):
        chain_count_larger=0
        chain_count_smaller=0
        for j in range(i):
            if pairs[j][1]>=pairs[i][0]:
                if result[j]>chain_count_larger:
                    chain_count_larger=result[j]
            if pairs[j][1]<pairs[i][0]:
                if result[j]>chain_count_smaller:
                    chain_count_smaller=result[j]
            result[i]=max(chain_count_larger, chain_count_smaller+1)
    return result[-1]

if __name__=='__main__':
    pairs=[[1,2],[7,8],[4,5]]
    print(findLongestChain(pairs))

