## 234. Palindrome Linked List

## Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

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

def isPalindrome(head):
    hare=head.next
    if hare:
        hare=hare.next
    tortoise=head
    while hare:
        hare=hare.next
        if hare:
            hare=hare.next
        tortoise=tortoise.next
    pre=None
    cur=tortoise.next
    tortoise.next=None
    while cur:
        nxt=cur.next
        cur.next=pre
        pre=cur
        cur=nxt
    node=head
    while pre and node:
        if node.val!=pre.val:
            return False
        node=node.next
        pre=pre.next
    return True

if __name__=='__main__':
    head = [1,2,3,4,5]
    node=None
    for val in head[::-1]:
        node=ListNode(val, node)
    head=node
    print(isPalindrome(head))