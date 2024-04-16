## 129. Sum Root to Leaf Numbers

# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):
    return sum([int(s) for s in dfs(root)])

def dfs(node):
    if not node.left and not node.right:
        return [str(node.val)]
    if node.left:
        l=dfs(node.left)
    else:
        l=[]
    if node.right:
        r=dfs(node.right)
    else:
        r=[]
    res=l+r
    return [str(node.val)+s for s in res]

def tree(i,ls):
    node=TreeNode(ls[i])
    if 2*i+1<=len(ls)-1:
        node.left=tree(2*i+1,ls)
    if 2*i+2<=len(ls)-1:
        node.right=tree(2*i+2,ls)
    return node

if __name__=="__main__":
    ls = [4,9,0,5,1]
    root=tree(0,ls)
    print(sumNumbers(root))