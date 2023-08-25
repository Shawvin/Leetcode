## 86. Partition List

## Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

## You should preserve the original relative order of the nodes in each of the two partitions.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    small=[]
    big=[]
    curr=head
    while(curr is not None):
        if curr.val<x:
            small.append(curr.val)
        else:
            big.append(curr.val)
        curr=curr.next
    result=small+big
    curr=head
    for i in range(len(result)):
        curr.val=result[i]
        curr=curr.next
    return head

if __name__=='__main__':
    head=[1,4,3,2,5,2]
    node=None
    for val in head[::-1]:
        node=ListNode(val, node)
    head=node
    result=partition(head, 3)
    while (result is not None):
        print(result.val)
        result=result.next