## 988. Smallest String Starting From Leaf
import string

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

def smallestFromLeaf(root):
    def dfs(node):
        if not node.left and not node.right:
            return [string.ascii_lowercase[node.val]]
        elif node.left and not node.right:
            l=dfs(node.left)
            return [x+string.ascii_lowercase[node.val] for x in l]
        elif node.right and not node.left:
            r=dfs(node.right)
            return [x+string.ascii_lowercase[node.val] for x in r]
        else:
            l=dfs(node.left)
            r=dfs(node.right)
            return [x+string.ascii_lowercase[node.val] for x in l+r]
    
    res=min(dfs(root))
    return res

class Tree:
    def __init__(self, root):
        root=self.tree(0, root)

    def tree(self, i, ls):
        node=TreeNode(ls[i])
        if 2*i+1<len(ls) and ls[2*i+1] is not None:
            node.left=self.tree(2*i+1, ls)
        if 2*i+2<len(ls) and ls[2*i+2] is not None:
            node.right=self.tree(2*i+2, ls)
        return node


if __name__=='__main__':
    root = [0,1,2,3,4,3,4]
    root=Tree(root).tree(0, root)
    print(smallestFromLeaf(root))