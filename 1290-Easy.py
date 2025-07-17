## 1290. Convert Binary Number in a Linked List to Integer

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def getDecimalValue(head) -> int:
    res=0
    cur=head
    while cur:
        res*=2
        res+=cur.val
        cur=cur.next
    return res


if __name__=='__main__':
    head = [1,0,1]
    node=None
    for val in head[::-1]:
        node=ListNode(val,node)
    head=node
    print(getDecimalValue(head))