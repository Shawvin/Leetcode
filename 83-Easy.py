## 83. Remove Duplicates from Sorted List

## Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class ListNode:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
    
    def __str__(self) -> str:
        node=self
        res=[]
        while node:
            res.append(str(node.val))
            node=node.next
        return '['+','.join(res)+']'

def deleteDuplicates(head):
    cur=head
    while cur:
        if cur.next and cur.next.val==cur.val:
            cur.next=cur.next.next
        else:
            cur=cur.next
    return head

if __name__=='__main__':
    head = [1,1,2,3,3]
    node=None
    for val in head[::-1]:
        node=ListNode(val,node)
    head=node
    print(deleteDuplicates(head))