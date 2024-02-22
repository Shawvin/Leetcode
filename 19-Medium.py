## 19. Remove Nth Node From End of List

## Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

    def __str__(self) -> str:
        return str(self.val)

def printList(node):
    l=[]
    while node:
      l.append(node.val)
      node = node.next
    print(l)

def removeNthFromEnd(head, n):
    p1=head
    p2=head
    count=n
    while p2.next:
        p2=p2.next
        count-=1
        if count==0:
            break
    if count>0:
        head=head.next
        return head
    while p2.next:
        p2=p2.next
        p1=p1.next
    p1.next=p1.next.next
    return head

if __name__=='__main__':
    l=[1,2,3,4,5]
    head=None
    for i in l[::-1]:
        head=ListNode(i,head)
    n=2
    printList(removeNthFromEnd(head, n))