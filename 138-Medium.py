## 138. Copy List with Random Pointer

## A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
## Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value 
## of its corresponding original node.

class Node:
    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(self, head):
    dummy=Node(0)
    cur=head
    node_dict={}
    if head is None:
        return None
    dummy.next=Node(head.val)
    cur_new=dummy.next
    node_dict[head]=cur_new
    while cur:
        if cur.next is None:
            cur_new.next=None
        elif cur.next in node_dict:
            cur_new.next=node_dict[cur.next]
        else:
            p=Node(cur.next.val)
            cur_new.next=p
            node_dict[cur.next]=p
        if cur.random is None:
            cur_new.random=None
        elif cur.random in node_dict:
            cur_new.random=node_dict[cur.random]
        else:
            q=Node(cur.random.val)
            node_dict[cur.random]=q
            cur_new.random=q
        cur_new=cur_new.next
        cur=cur.next
    return dummy.next