## 2073. Time Needed to Buy Tickets

def timeRequiredToBuy(tickets, k):
    count=0
    while tickets[k]!=0:
        for i in range(len(tickets)):
            if tickets[i]>0:
                tickets[i]-=1
                count+=1
            if tickets[k]==0:
                break
    return count

def timeRequiredToBuy2(tickets, k):
    return sum([min(tickets[k], tickets[i]) if i<=k else min(tickets[k]-1, tickets[i]) for i in range(len(tickets))])

if __name__=='__main__':
    tickets = [84,49,5,24,70,77,87,8]
    k=3
    print(timeRequiredToBuy(tickets, k))