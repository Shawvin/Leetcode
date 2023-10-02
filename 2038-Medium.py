## 2038. Remove Colored Pieces if Both Neighbors are the Same Color

## There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. 
## You are given a string colors of length n where colors[i] is the color of the ith piece.

def winnerOfGame(colors):
    n=len(colors)
    chances={'A':0, 'B':0}
    count=1
    for cur in range(1,n):
        pre=cur-1
        if colors[cur]==colors[pre]:
            count+=1
        else:
            chances[colors[pre]]+=max(0, count-2)
            count=1
    chances[colors[-1]]+=max(0, count-2)
    return chances['A']>chances['B']

if __name__=='__main__':
    colors = "AAABABB"
    print(winnerOfGame(colors))