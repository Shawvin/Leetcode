## 206. Reverse Linked List

## Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

    def __str__(self):
        node=self
        res=[]
        while node:
            res.append(str(node.val))
            node=node.next
        return ','.join(res)
    
def reverseList(head):
    if not head:
        return head
    pre=None
    cur=head
    nxt=head.next
    while nxt:
        cur.next=pre
        pre=cur
        cur=nxt
        nxt=nxt.next
    cur.next=pre
    return cur

## iterative
def reverseList2(head):
    cur=head
    pre=None
    while cur:
        nxt=cur.next
        cur.next=pre
        pre=cur
        cur=nxt
    return pre

## recursive
def reverseList3(head):
    if not head or not head.next:
        return head
    
    h2=reverseList(head.next)
    head.next.next=head
    head.next=None
    return h2

if __name__=='__main__':
    head = [1,2,3,4,5]
    node=None
    for val in head[::-1]:
        node=ListNode(val, node)
    head=node
    print(reverseList3(head))

