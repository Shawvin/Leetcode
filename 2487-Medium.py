## 2487. Remove Nodes From Linked List

## You are given the head of a linked list.

## Remove every node which has a node with a greater value anywhere to the right side of it.
## Return the head of the modified linked list.

class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
    def __str__(self):
        res=[]
        res.append(str(self.val))
        nxt=self.next
        while nxt:
            res.append(str(nxt.val))
            nxt=nxt.next
        return ','.join(res)        

class Linkedlist:
    def __init__(self, head=None) -> None:
        node=None
        for i in head[::-1]:
            node=ListNode(i,node)
        self.head=node

def removeNodes(head):
    head=reverse(head)
    cur=head
    while cur:
        nxt=cur.next
        while nxt and nxt.val<cur.val:
            nxt=nxt.next
        cur.next=nxt
        cur=cur.next
    head=reverse(head)
    return head

def reverse(head):
    pre=None
    cur=head
    nxt=head.next
    while nxt:
        cur.next=pre  
        pre=cur
        cur=nxt
        nxt=nxt.next
    cur.next=pre   
    head=cur
    return head

def removeNodes2(head):
    st=[]
    cur=head
    while cur:
        st.append(cur)
        cur=cur.next
    cur_max=0
    last=None
    while len(st)>0:
        cur=st.pop()
        if cur.val>=cur_max:
            cur.next=last
            last=cur
            cur_max=cur.val
    return last

if __name__=='__main__':
    head = [5,2,13,3,8]
    ll=Linkedlist(head)
    print(removeNodes2(ll.head))