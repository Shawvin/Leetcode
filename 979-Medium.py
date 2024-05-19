## 979. Distribute Coins in Binary Tree

## You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.
## In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.
## Return the minimum number of moves required to make every node have exactly one coin.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right    

def distributeCoins(root):
    def f(root, parent):
        if root==None: return 0
        moves=f(root.left, root)+f(root.right, root)
        x=root.val-1
        if parent!=None: parent.val+=x
        moves+=abs(x)
        return moves
    return f(root, None)

def tree(l, idx):
    if idx<len(l):
        node=TreeNode(l[idx], left=tree(l,2*idx+1), right=tree(l,2*idx+2))
        return node
    else:
        return None

if __name__=='__main__':
    root = [0,3,0]
    root=tree(root,0)
    print(distributeCoins(root))