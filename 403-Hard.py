## 403. Frog Jump
## A frog is crossing a river. The river is divided into some number of units, and at each unit, 
## there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

def canCross(stones):
    if stones[1]!=1:
        return False
    index_dict={}
    for i in range(len(stones)):
        index_dict[stones[i]]=i
    steps=[set() for i in range(len(stones))]
    steps[1].add(1)
    for i in range(1, len(stones)):
        for k in steps[i]:
            for step in range(k-1,k+2):
                if step and (stones[i]+step in index_dict):
                    steps[index_dict.get(stones[i]+step)].add(step)
    print(steps)
    return len(steps[-1])>0

if __name__=='__main__':
    stones = [0,1,3,6,7]
    print(canCross(stones))