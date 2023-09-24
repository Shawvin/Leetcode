## 799. Champagne Tower

## after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

def champagneTower(poured, query_row, query_glass):
    pre_row=[poured]
    new_row=pre_row
    for i in range(1, query_row+1):
        new_row=[0]*(i+1)
        for j in range(i+1):
            if j==0:
                new_row[j]=max(pre_row[0]-1,0)/2
            elif j==i:
                new_row[j]=max(pre_row[-1]-1,0)/2
            else:
                new_row[j]=(max(pre_row[j-1]-1,0))/2+(max(pre_row[j]-1,0))/2
        pre_row=new_row
    return min(new_row[query_glass], 1)

if __name__=='__main__':
    poured = 100000009
    query_row = 33
    query_glass = 17
    print(champagneTower(poured, query_row, query_glass))