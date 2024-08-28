## 840. Magic Squares In Grid

def numMagicSquaresInside(grid):
    row=len(grid)
    col=len(grid[0])
    res=0
    for i in range(row-2):
        for j in range(col-2):
            if checked(grid, i, j):
                res+=1
    return res

def checked(grid,i,j):
    temp=set()
    for k in range(i,i+3):
        temp.add(grid[k][j])
        temp.add(grid[k][j+1])
        temp.add(grid[k][j+2])
        if sum(grid[i][j:j+3])!=15:
            return False
    for l in range(j,j+3):
        if grid[i][j]+grid[i+1][j]+grid[i+2][j]!=15:
            return False
    if grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]!=15:
            return False
    if grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]!=15:
            return False
    if len(temp)<9 or max(temp)!=9 or min(temp)!=1:
        return False
    return True

if __name__=='__main__':
    grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
    print(numMagicSquaresInside(grid))