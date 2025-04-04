#1123. Lowest Common Ancestor of Deepest Leaves
import heapq
from collections import defaultdict

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def constructTree(l):
     def addNode(idx, l):
          if idx>=len(l) or l[idx] is None:
               return None
          node=TreeNode(l[idx])
          node.left=addNode(2*idx+1, l)
          node.right=addNode(2*idx+2, l)
          return node
     
     return addNode(0,l)

def lcaDeepestLeaves(root):
     def dfs(node):
        if not node.left and not node.right:
            return (node, 0)
        ld=0
        rd=0
        if node.left:
            lca, ld = dfs(node.left)
            ld+=1
        if node.right:
            rca, rd = dfs(node.right)
            rd+=1
        if ld>rd:
            return lca, ld
        elif ld<rd:
            return rca, rd
        else:
            return node, ld
        
     return dfs(root)[0]
        
if __name__=='__main__':
     l = [3,5,1,6,2,0,8,None,None,7,4]
     root = constructTree(l)
     print(lcaDeepestLeaves(root).val)