## 2139. Minimum Moves to Reach Target Score

def minMoves(target, maxDoubles):
    count=0
    while target!=1:
        if target%2==0 and maxDoubles>0:
            target=target//2
            maxDoubles-=1
            count+=1
        elif maxDoubles==0:
            count+=(target-1)
            target=1
        else:
            target-=1
            count+=1
    return count

if __name__=='__main__':
    target = 656101987
    maxDoubles = 1
    print(minMoves(target, maxDoubles))