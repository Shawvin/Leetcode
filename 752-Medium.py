## 752. Open the Lock

def openLock(deadends, target):
    q=[]
    step={}
    if '0000' not in deadends:
        q.append('0000')
        deadends.append('0000')
        step['0000']=0
    while q:
        cur=q.pop(0)
        if cur==target:
            return step[cur]
        for i in range(4):
            change=int(cur[i])+1
            if change>9:
                change-=10
            next=cur[:i]+str(change)+cur[i+1:]
            if next not in deadends and next not in step:
                step[next]=step[cur]+1
                q.append(next)
            change=int(cur[i])-1
            if change<0:
                change+=10
            next=cur[:i]+str(change)+cur[i+1:]
            if next not in deadends and next not in step:
                step[next]=step[cur]+1
                q.append(next)
    return -1

if __name__=='__main__':
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    print(openLock(deadends, target))