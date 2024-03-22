## 92. Reverse Linked List II

## Given the head of a singly linked list and two integers left and right where left <= right, 
## reverse the nodes of the list from position left to position right, and return the reversed list.

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
    
def reverseBetween(head, left, right):
    count=1
    dummy=ListNode(0,head)
    left_pre=dummy
    left_idx=head

    while count<left:
        left_idx=left_idx.next
        left_pre=left_pre.next
        count+=1
    left_stop=left_pre
    left_pre=None
    right_stop=left_idx
    while count<right+1:
        left_nxt=left_idx.next
        left_idx.next=left_pre
        left_pre=left_idx
        left_idx=left_nxt
        count+=1
    right_stop.next=left_idx
    left_stop.next=left_pre
    return dummy.next

if __name__=='__main__':
    head = [1,2,3,4,5]
    node=None
    for val in head[::-1]:
        node=ListNode(val, node)
    head=node
    left=2
    right=4
    print(reverseBetween(head, left, right))