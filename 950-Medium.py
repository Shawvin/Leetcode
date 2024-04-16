## 950. Reveal Cards In Increasing Order

## reverse process
def deckRevealedIncreasing(deck):
    deck.sort(key=lambda x:-x)
    res=[]
    for num in deck:
        if len(res)>0:
            res.insert(0, res.pop())
        res.insert(0, num)
    return res

## forward simulation
def deckRevealedIncreasing2(deck):
    deck.sort()
    res=[0]*len(deck)
    sim=list(range(len(deck)))
    i=0
    while len(sim)>0:
        cur=sim.pop(0)
        res[cur]=deck[i]
        i+=1
        if len(sim)>0:
            sim.append(sim.pop(0))
    return res

if __name__=="__main__":
    deck=[17,13,11,2,3,5,7]
    print(deckRevealedIncreasing(deck))