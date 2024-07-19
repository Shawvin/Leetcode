## 2049. Count Nodes With the Highest Score

from collections import defaultdict

def countHighestScoreNodes(parents):
    map=defaultdict(list)
    for i,num in enumerate(parents):
        map[num].append(i)
    size=[0]*len(parents)
    def subtreeSize(idx, size):
        if size[idx]!=0:
            return size[idx]
        count=1
        for child in map[idx]:
            count+=subtreeSize(child, size)
        size[idx]=count
        return count
    max_product=0
    res=0
    for i in range(len(parents)):
        root=len(parents)-1
        prod=1
        for child in map[i]:
            childSize=subtreeSize(child, size)
            prod*=childSize
            root-=childSize
        if root>0:
            prod*=root
        if prod==max_product:
            res+=1
        if prod>max_product:
            res=1
            max_product=prod
    return res

if __name__=='__main__':
    parents = [-1,2,0,2,0]
    print(countHighestScoreNodes(parents))