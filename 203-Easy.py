## 203. Remove Linked List Elements

## Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    dummy=ListNode(0,head)
    pre=dummy
    cur=head
    while cur:
        if cur.val==val:
            pre.next=cur.next
        else:
            pre=cur
        cur=cur.next
    return dummy.next

if __name__=='__main__':
    headlist = [1,2,6,3,4,5,6]
    val=6
    head=None
    for i in headlist[::-1]:
        head=ListNode(i,head)
    print(removeElements(head, val))