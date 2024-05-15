## 2373. Largest Local Values in a Matrix

def largestLocal(grid):
    n=len(grid)
    res=[[0 for j in range(n-2)] for i in range(n-2)]
    for i in range(n-2):
        for j in range(n-2):
            max_grid=res[i][j]
            for x in range(i,i+3):
                for y in range(j, j+3):
                    max_grid=max(max_grid, grid[x][y])
            res[i][j]=max_grid
    return res

def largestLocal2(grid):
    n=len(grid)
    res=[[max(grid[j][i-1:i+2]) for i in range(1, n-1)] for j in range(n)]
    res=[[max(x[i] for x in res[j-1:j+2]) for i in range(n-2)] for j in range(1, n-1)]
    return res

if __name__=='__main__':
    grid=[[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    print(largestLocal2(grid))