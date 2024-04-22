## 1654. Minimum Jumps to Reach Home

def minimumJumps(forbidden, a, b, x):
    q=[]
    dir=1
    q.append((0,1))
    count={}
    max_val=max([x]+forbidden) +a+b
    forbidden=set(forbidden)
    visit={}
    visit[0]=True
    count[0]=0
    while q:
        cur, dir=q.pop(0)
        if cur==x:
            return count[cur]
        if dir>0:
            if cur-b>=0 and cur-b not in forbidden and cur-b not in visit:
                visit[cur-b]=True
                q.append((cur-b,-1))
                count[cur-b]=count[cur]+1
            if cur+a<=max_val and cur+a not in forbidden and cur+a not in visit:
                visit[cur+a]=True
                q.append((cur+a,1))
                count[cur+a]=count[cur]+1
        if dir<0:
            if cur+a<=max_val and cur+a not in forbidden and cur+a not in visit:
                visit[cur+a]=True
                q.append((cur+a,1))
                count[cur+a]=count[cur]+1
    return -1

if __name__=='__main__':
    forbidden = [14,4,18,1,15]
    a = 3 
    b = 15
    x = 9
    print(minimumJumps(forbidden, a, b, x))