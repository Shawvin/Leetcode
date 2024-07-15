## 109. Convert Sorted List to Binary Search Tree

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Linkedlist(l):
    cur=None
    for val in l[::-1]:
        cur=ListNode(val,cur)
    return cur

def sortedListToBST(head):
    def Tree(l):
        if len(l)==0:
            return None
        else:
            mid=len(l)//2
            node=ListNode(l[mid])
            node.left=Tree(l[:mid])
            node.right=Tree(l[mid+1:])
        return node
    l=[]
    cur=head
    while cur:
        l.append(cur.val)
        cur=cur.next
    return Tree(l)

def sortedListToBST2(head):
    def Tree(cur):
        if not cur:
            return None
        if not cur.next:
            return TreeNode(cur.val)
        t=cur
        h=cur.next
        if h:
            h=h.next
        while h:
            h=h.next
            if h:
                h=h.next
            else:
                break
            t=t.next
        mid=t.next
        t.next=None
        node=TreeNode(mid.val)
        node.left=Tree(cur)
        node.right=Tree(mid.next)
        return node
    return Tree(head)

def traverse(root):
    res=[]
    q=[root]
    while q:
        l=len(q)
        for i in range(l):
            node=q.pop(0)
            if not node:
                res.append(None)
                continue
            else:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            elif node.right:
                q.append(None)
            if node.right:
                q.append(node.right)
            elif node.left:
                q.append(None)
    return res

if __name__=='__main__':
    head = [-10,-3,0,5,9]
    head = Linkedlist(head)
    print(traverse(sortedListToBST(head)))