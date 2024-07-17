## 1110. Delete Nodes And Return Forest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructTree(l,i):
    node=l[i]
    if 2*i+1<len(l) and l[2*i+1] is not None:
        node.left=constructTree(l,2*i+1)
    if 2*i+2<len(l) and l[2*i+2] is not None:
        node.right=constructTree(l,2*i+2)

def delNodes(root, to_delete):
    to_delete = set(to_delete)
    q=[root]
    res=[]
    if root.val not in to_delete:
        res.append(root)
    while len(q)>0:
        cur=q.pop(0)
        if cur.left:
            q.append(cur.left)
            if cur.left.val in to_delete:
                cur.left=None
        if cur.right:
            q.append(cur.right)
            if cur.right.val in to_delete:
                cur.right=None
        if cur.val in to_delete:
            if cur.left:
                res.append(cur.left)
            if cur.right:
                res.append(cur.right)
    return res

def delNodes2(root, to_delete):
    to_delete = set(to_delete)
    res=[]
    def delNode(root, to_delete, no_parent):
        if not root:
            return None
        delete=(root.val in to_delete)
        root.left=delNode(root.left, to_delete, delete)
        root.right=delNode(root.right, to_delete, delete)
        if delete:
            return None
        elif no_parent:
            res.append(root)
        return root
    delNode(root, to_delete, True)
    return res

if __name__=='__main__':
    root = [1,2,4,None,3]
    root = constructTree(root,0)
    to_delete = [3]
    print(delNodes(root, to_delete))