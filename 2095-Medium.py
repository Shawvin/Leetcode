## 2095. Delete the Middle Node of a Linked List

## You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
## The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
## For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head):
    second=head
    first=head.next
    if first:
        first=first.next
    else:
        return None
    while first:
        if not first.next:
            second.next=second.next.next
            return head
        first=first.next.next
        second=second.next
    second.next=second.next.next
    return head

if __name__=='__main__':
    lst=[1,2,3,4,5,6]
    node=ListNode(lst[0])
    head=node
    for i in lst[1:]:
        node.next=ListNode(i)
        node=node.next
    result=deleteMiddle(head)
    lst=[]
    while result:
        lst.append(result.val)
        result=result.next
    print(lst)