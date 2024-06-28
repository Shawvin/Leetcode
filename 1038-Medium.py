## 1038. Binary Search Tree to Greater Sum Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        st=[root]
        res=[]
        while len(st)>0:
            cur=st.pop(0)
            res.append(str(cur.val))
            if cur.left:
                st.append(cur.left)
            if cur.right:
                st.append(cur.right)
        return ' '.join(res)

def bstToGst(root):
    cur=root
    st=[]
    cumsum=0
    while len(st)>0 or cur:
        if cur:
            st.append(cur)
            cur=cur.right
        else:
            cur=st.pop()
            cur.val+=cumsum
            cumsum=cur.val
            cur=cur.left
    return root

def bstToGst2(root):
    def updateTree(node, cumsum):
        if not node:
            return cumsum
        rightsum=updateTree(node.right, cumsum)
        node.val+=rightsum
        leftsum=updateTree(node.left, node.val)
        return leftsum
    updateTree(root, 0)
    return root

def constructNode(l, idx):
    if l[idx] is None:
        return None
    node = TreeNode(l[idx])
    if 2*idx+1<len(l):
        node.left = constructNode(l, 2*idx+1)
    if 2*idx+2<len(l):
        node.right = constructNode(l, 2*idx+2)
    return node


if __name__=='__main__':
    root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    root = constructNode(root,0)
    print(bstToGst(root))