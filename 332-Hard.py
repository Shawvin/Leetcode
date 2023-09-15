## 332. Reconstruct Itinerary

## You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. 
## Reconstruct the itinerary in order and return it.

from collections import defaultdict
def findItinerary(tickets):
    tickets=sorted(tickets, reverse=True)
    print(tickets)

    iter_dict=defaultdict(list)
    temp=[]
    for ticket in tickets:
        iter_dict[ticket[0]].append(ticket[1])
    print(iter_dict)
    
    def dfs(airport):
        while iter_dict[airport]:
            dfs(iter_dict[airport].pop())
        temp.append(airport)
    
    dfs("JFK")
    return temp[::-1]

if __name__=='__main__':
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    print(findItinerary(tickets))