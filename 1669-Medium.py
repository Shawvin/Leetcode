## 1669. Merge In Between Linked Lists

## You are given two linked lists: list1 and list2 of sizes n and m respectively.
## Remove list1's nodes from the ath node to the bth node, and put list2 in their place. 
## The blue edges and nodes in the following figure indicate the result:

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

def mergeInBetween(list1, a, b, list2):
    list2e=list2
    while list2e.next:
        list2e=list2e.next
    list1a=list1
    list1b=list1
    count=0
    while count<b:
        if count<a-1:
            list1a=list1a.next
        list1b=list1b.next
        count+=1
    list1a.next=list2
    list2e.next=list1b.next
    list1b.next=None
    return list1

if __name__=='__main__':
    list1 = [10,1,13,6,9,5]
    a = 3
    b = 4
    list2 = [1000000,1000001,1000002]
    node1=None
    for val in list1[::-1]:
        node1=ListNode(val, node1)
    list1=node1
    node2=None
    for val in list2[::-1]:
        node2=ListNode(val, node2)
    list2=node2
    print(mergeInBetween(list1, a, b, list2))
