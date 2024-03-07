## 876. Middle of the Linked List

## Given the head of a singly linked list, return the middle node of the linked list.
## If there are two middle nodes, return the second middle node.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle(head):
    second=head.next
    if second:
        first=second.next
    else:
        return head
    while first:
        if not first.next:
            break
        first=first.next.next
        second=second.next
    return second

if __name__=='__main__':
    lst=[1,2,3,4,5,6]
    node=ListNode(lst[0])
    head=node
    for i in lst[1:]:
        node.next=ListNode(i)
        node=node.next
    result=middle(head)
    lst=[]
    while result:
        lst.append(result.val)
        result=result.next
    print(lst)