## 404. Sum of Left Leaves

## Given the root of a binary tree, return the sum of all left leaves.
## A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def sumOfLeftLeaves(root):
    total=0
    st=[]
    cur=root
    while st or cur:
        if cur:
            st.append(cur.right)
            cur=cur.left
            if cur and not cur.left and not cur.right:
                total+=cur.val
        else:
            cur=st.pop()
    return total

def recur(i,ls):
    if ls[i]:
        node=TreeNode(ls[i])
    else:
        return None
    if 2*i+1<=len(ls)-1:
        node.left=recur(2*i+1,ls)
    if 2*i+2<=len(ls)-1:
        node.right=recur(2*i+2,ls)
    return node


if __name__=='__main__':
    ls=[3,9,20,None,None,15,7]
    root=recur(0,ls)
    print(sumOfLeftLeaves(root))