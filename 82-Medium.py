## 82. Remove Duplicates from Sorted List II

## Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
## leaving only distinct numbers from the original list. Return the linked list sorted as well.

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
    if not head:
        return head
    dummy=ListNode(-101, head)
    cur=dummy
    pre=head
    next=head.next
    cur_val=head.val
    count=1
    while next:
        if next.val!=cur_val:
            if count==1:
                cur.next=pre
                cur=pre
            cur_val=next.val
            count=1
        else:
            count+=1
        pre=next
        next=next.next
    if count==1:
        cur.next=pre
    else:
        cur.next=None
    return dummy.next

def deleteDuplicates2(head):
    if not head:
        return head
    dummy=ListNode(-101, head)
    pre=dummy
    cur=head
    flag=False
    while cur:
        while cur.next and cur.next.val==cur.val:
            flag=True
            cur=cur.next
        if not flag:
            pre.next=cur
            pre=pre.next
        cur=cur.next
        flag=False
    pre.next=cur
    return dummy.next

if __name__=='__main__':
    head = [1,1,2,3,3]
    node=None
    for val in head[::-1]:
        node=ListNode(val,node)
    head=node
    print(deleteDuplicates(head))