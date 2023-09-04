## 141. Linked List Cycle

## Given head, the head of a linked list, determine if the linked list has a cycle in it.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def hasCycle(head):
    if not head:
        return False
    hare=head.next
    if hare:
        hare=hare.next
    tortoise=head.next
    while hare:
        if tortoise==hare:
            return True
        tortoise=tortoise.next
        hare=hare.next
        if hare:
            hare=hare.next
    return False

if __name__=='__main__':
    head=[3,2,0,-4]
    pos=1
    dummy=ListNode(0)
    pre=dummy
    for val in head:
        cur=ListNode(val)
        pre.next=cur
        pre=cur
    end=pre
    pre=dummy.next
    head=dummy.next
    if pos>0:
        for i in range(pos):
            pre=pre.next
        end.next=pre
    print(hasCycle(head))