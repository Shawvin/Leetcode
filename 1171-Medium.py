## 1171. Remove Zero Sum Consecutive Nodes from Linked List

## Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

## After doing so, return the head of the final linked list.  You may return any such answer.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        l=[]
        node=self
        while node:
            l.append(str(node.val))
            node=node.next
        return ','.join(l)

def removeZeroSumSublists(head):
    arraylist=[]
    node=head
    while node:
        arraylist.append(node.val)
        node=node.next
    idx=0
    idx2=idx
    remove_idx=[]
    while idx<len(arraylist):
        cum_sum=0
        while idx2<len(arraylist):
            cum_sum+=arraylist[idx2]
            if cum_sum==0:
                remove_idx.extend(range(idx,idx2+1))
                idx=idx2
                break
            idx2+=1
        idx+=1
        idx2=idx
    res=[arraylist[i] for i in range(len(arraylist)) if i not in remove_idx]
    if res:
        head=ListNode(res[0])
        node=head
    else:
        return None
    for val in res[1:]:
        node.next=ListNode(val)
        node=node.next
    return head

def removeZeroSumSublists2(head):
    dummy=ListNode(0, head)
    node=head
    pre_sum={}
    pre_sum[0]=dummy
    cum_sum=0
    while node:
        cum_sum+=node.val
        if cum_sum in pre_sum:
            start=pre_sum[cum_sum]
            temp=start.next
            temp_sum=cum_sum
            while temp!=node:
                temp_sum+=temp.val
                pre_sum.pop(temp_sum)
                temp=temp.next
            start.next=node.next
            node=node.next
        else:
            pre_sum[cum_sum]=node
            node=node.next
    return dummy.next

if __name__=='__main__':
    head=[1,2,3,-3,4]
    if head:
        dummy=ListNode(head[0])
        node=dummy
    else:
        head=None
    for val in head[1:]:
        node.next=ListNode(val)
        node=node.next
    head=dummy
    print(removeZeroSumSublists2(head))