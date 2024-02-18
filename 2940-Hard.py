## 2940. Find Building Where Alice and Bob Can Meet

## You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.
## If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].
## You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.
## Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. 
## If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

def leftmostBuildingQueries(heights, queries):
    result=[]
    stack=[0]
    next_high=[-1]*len(heights)
    for i in range(1,len(heights)):
        while stack and heights[stack[-1]]<heights[i]:
            curr=stack.pop()
            next_high[curr]=i
        stack.append(i)
    for i, j in queries:
        if i>j:
            i,j=j,i
        if heights[j]>heights[i] or i==j:
            result.append(j)
            continue
        curr=j
        while next_high[curr]!=-1 and heights[curr]<=heights[i]:
            curr=next_high[curr]
        if heights[curr]>heights[i]:
            result.append(curr)
        else:
            result.append(-1)
    return result

def leftmostBuildingQueries2(heights, queries):
    for i,query in enumerate(queries):
        query.append(i)
        if query[0]>query[1]:
            query[0], query[1]=query[1], query[0]
    queries=sorted(queries, key=lambda x: -x[1])
    i=len(heights)-1
    stack=[]
    ret=[-1]*len(queries)
    for query in queries:
        a, b, q_idx=query
        if heights[b]>heights[a] or a==b:
            ret[q_idx]=b
            continue
        while i>b:
            if len(stack)>0 and heights[i]>=stack[0][0]:
                stack.pop(0)
            else:
                stack.insert(0, (heights[i],i))
                i-=1
        for h, idx in stack:
            if h>heights[a]:
                checked=True
                ret[q_idx]=idx
                break
    return ret

def leftmostBuildingQueries3(heights, queries):
    for i,query in enumerate(queries):
        query.append(i)
        if query[0]>query[1]:
            query[0], query[1]=query[1], query[0]
    queries=sorted(queries, key=lambda x: -x[1])
    
    i=len(heights)-1
    stack=[]
    ret=[-1]*len(queries)
    for query in queries:
        a, b, q_idx=query
        if heights[b]>heights[a] or a==b:
            ret[q_idx]=b
            continue
        while i>b:
            if len(stack)>0 and heights[i]>=stack[0][0]:
                stack.pop(0)
            else:
                stack.insert(0, (heights[i],i))
                i-=1
        l,r=0,len(stack)-1
        if len(stack)==0:
            continue
        while l<r:
            m=(l+r)//2
            if stack[m][0]>heights[a]:
                r=m
            elif stack[m][0]<heights[a]:
                l=m+1
            else:
                ret[q_idx]=stack[m+1][1]
                break
        if stack[l][0]>heights[a]:
            ret[q_idx]=stack[l][1]
            continue
        if stack[r][0]>heights[a]:
            ret[q_idx]=stack[r][1]
            continue
    return ret

if __name__=='__main__':
    heights = [6,4,8,5,2,7]
    queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
    print(leftmostBuildingQueries3(heights, queries))

