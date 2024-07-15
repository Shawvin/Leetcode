## 2196. Create Binary Tree From Descriptions

from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree(descriptions):
    def Tree(map, nodeVal):
        node=TreeNode(nodeVal)
        if len(map[nodeVal])==0:
            return node
        if map[nodeVal][0]:
            node.left=Tree(map, map[nodeVal][0])
        if map[nodeVal][1]:
            node.right=Tree(map, map[nodeVal][1])
        return node
        
    map=defaultdict(list)
    inDegree={}
    for p, c, left in descriptions:
        if p not in map:
            map[p]=[None, None]
        if left:
            map[p][0]=c
        else:
            map[p][1]=c
        inDegree[c]=1
        if p not in inDegree:
            inDegree[p]=0
    for k in inDegree:
        if inDegree[k]==0:
            root=k
            break
    return Tree(map, root)

def traverse(root):
    res=[]
    q=[root]
    while q:
        l=len(q)
        for i in range(l):
            node=q.pop(0)
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res

if __name__=='__main__':
    descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    print(traverse(createBinaryTree(descriptions)))