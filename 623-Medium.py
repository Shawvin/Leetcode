## 623. Add One Row to Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        st=[]
        res=[]
        cur=self
        while len(st)>0 or cur:
            if cur:
                res.append(str(cur.val))
            else:
                res.append('null')
            if cur and cur.left:
                st.append(cur.left)
            if cur and cur.right:
                st.append(cur.right)
            if len(st)>0:
                cur=st.pop(0)
            else:
                cur=None
        return ','.join(res)

def addOneRow(root, val, depth):
    def dfs(node, count, depth, val, subtree):
        if count==depth-1:
            if subtree=='left':
                return TreeNode(val, left=node)
            else:
                return TreeNode(val, right=node)
        else:
            if node.left:
                node.left=dfs(node.left, count+1, depth, val, 'left')
            elif count==depth-2:
                node.left=TreeNode(val)
            if node.right:
                node.right=dfs(node.right, count+1, depth, val, 'right')
            elif count==depth-2:
                node.right=TreeNode(val)
            return node

    count=0
    if depth==1:
        return TreeNode(val, left=root)
    else:
        if root.left:
            root.left=dfs(root.left, count+1, depth, val, 'left')
        elif count==depth-2:
             root.left=TreeNode(val)
        if root.right:
            root.right=dfs(root.right, count+1, depth, val, 'right')
        elif count==depth-2:
             root.right=TreeNode(val)
        return root
    
def tree(i, ls):
    node=TreeNode(ls[i])
    if 2*i+1<len(ls) and ls[2*i+1] is not None:
        node.left=tree(2*i+1, ls)
    if 2*i+2<len(ls) and ls[2*i+2] is not None:
        node.right=tree(2*i+2, ls)
    return node

if __name__=='__main__':
    root = [4,2,None,3,1]
    val = 1
    depth = 3
    root=tree(0, root)
    print(addOneRow(root, val, depth))