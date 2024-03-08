## 143. Reorder List

## You are given the head of a singly linked-list. The list can be represented as:
## L0 → L1 → … → Ln - 1 → Ln
## Reorder the list to be on the following form:
## L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
## You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reorderList(head):
    tortoise=head
    if not head.next:
        return 
    hare=head.next.next
    while hare:
        if not hare.next:
            break
        hare=hare.next.next
        tortoise=tortoise.next
    second=tortoise.next
    tortoise.next=None
    reverse=[]
    while second:
        reverse.append(second)
        second=second.next
    node=reverse.pop()
    second=node
    while reverse:
        node.next=reverse.pop()
        node=node.next
    node.next=None
    first=head
    first2=head.next
    second2=second.next
    while second:
        if first:
            first.next=second
            second.next=first2
        if first2:
            first, first2=first2, first2.next
        else:
            first=first2
            second.next=second2
            break
        if second2:
            second, second2=second2, second2.next
        else:
            second=second2

if __name__=='__main__':
    head=[1,2,3,4,5]
    dummy=ListNode(0)
    node=dummy
    for val in head:
        node.next=ListNode(val)
        node=node.next
    head=dummy.next
    reorderList(head)
    lst=[]
    while head:
        lst.append(head.val)
        head=head.next
    print(lst)