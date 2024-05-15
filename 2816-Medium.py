## 2816. Double a Number Represented as a Linked List

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

def doubleIt(head):
    st=[]
    cur=head
    while cur:
        st.append(cur)
        cur=cur.next
    incre=0
    while len(st)>0:
        cur=st.pop()
        double=cur.val*2
        remainder=double%10
        cur.val=remainder+incre
        if double>9:
            incre=1
        else:
            incre=0
    if incre>0:
        head=ListNode(1,cur)
    else:
        head=cur
    return head

if __name__=='__main__':
    head = [1,8,9]
    ll = Linkedlist(head)
    print(doubleIt(ll.head))