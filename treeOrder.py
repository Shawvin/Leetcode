## treeOrder

list = [5, 4, 6, 1, 2, 7, 8]

class Node:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def constructTree(list):
    def node(list, idx):
        leafnode=Node(list[idx])
        if 2*idx+1<len(list):
            leafnode.left=node(list, 2*idx+1)
        if 2*idx+2<len(list):
            leafnode.right=node(list, 2*idx+2)
        return leafnode

    root=node(list,0)
    return root

def preOrder(tree):
    st=[]
    cur=tree
    res=[]
    while len(st)>0 or cur:
        if cur:
            res.append(cur.val)
            st.append(cur)
            cur=cur.left
        else:
            cur=st.pop().right
    print(res)

def inOrder(tree):
    st=[]
    cur=tree
    res=[]
    while len(st)>0 or cur:
        if cur:
            st.append(cur)
            cur=cur.left
        else:
            cur=st.pop()
            res.append(cur.val)
            cur=cur.right
    print(res)

def postOrder(tree):
    st=[]
    cur=tree
    res=[]
    while len(st)>0 or cur:
        if cur:
            res.append(cur.val)
            st.append(cur)
            cur=cur.right
        else:
            cur=st.pop().left
    print(res[::-1])

if __name__=='__main__':
    tree=constructTree(list)
    preOrder(tree)
    inOrder(tree)
    postOrder(tree)