## 2096. Step-By-Step Directions From a Binary Tree Node to Another

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def constructTree(root,k):
    node=TreeNode(root[k])
    if 2*k+1<len(root) and root[2*k+1]:
        node.left=constructTree(root,2*k+1)
    if 2*k+2<len(root) and root[2*k+2]:
        node.right=constructTree(root,2*k+2)
    return node

def getDirections(root, startValue, destValue):
    n=1
    q=[root]
    while len(q)>0:
        cur=q.pop(0)
        n+=1
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    visited=[False]*(n+1)
    pNode=[0]*(n+1)
    pPath=[None]*(n+1)
    st=[root]
    while not visited[startValue] or not visited[destValue]:
        cur=st.pop()
        visited[cur.val]=True
        if cur.left and not visited[cur.left.val]:
            st.append(cur.left)
            pNode[cur.left.val]=cur.val
            pPath[cur.left.val]='L'
        if cur.right and not visited[cur.right.val]:
            st.append(cur.right)
            pNode[cur.right.val]=cur.val
            pPath[cur.right.val]='R'
    s=[startValue]
    d=[]
    cur=startValue
    while pNode[cur]!=0:
        cur=pNode[cur]
        s.append(cur)
    cur=destValue
    while pNode[cur]!=0:
        if cur in s:
            break
        d.append(cur)
        cur=pNode[cur]
    res=''
    for i in s:
        if i==cur:
            break
        res+='U'
    for j in d[::-1]:
        if pPath[j]:
            res+=pPath[j]
    return res

if __name__=='__main__':
    root = [5,8,3,1,None,4,7,6,None,None,None,None,None,None,2]
    root = constructTree(root,0)
    startValue = 4
    destValue = 3
    print(getDirections(root, startValue, destValue))