## 515. Find Largest Value in Each Tree Row

## Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def largestValues(root):
    temp=list()
    if root:
        temp.append((root,0))
    else:
        return None
    row_list=[]
    while temp:
        node,idx=temp.pop()
        if len(row_list)<=idx:
            row_list.append([node.val])
        else:
            row_list[idx].append(node.val)
        if node.left:
            temp.append((node.left,idx+1))
        if node.right:
            temp.append((node.right,idx+1))
    return [max(x) for x in row_list]

def construct_tree(tree_list, idx):
    if idx<len(tree_list) and tree_list[idx] is not None:
        cur=TreeNode(tree_list[idx])
    else:
        return None
    cur.left=construct_tree(tree_list, idx*2+1)
    cur.right=construct_tree(tree_list, idx*2+2)
    return cur
    

if __name__=='__main__':
    tree_list=[1,2,3]
    root=construct_tree(tree_list,0)
    print(largestValues(root))