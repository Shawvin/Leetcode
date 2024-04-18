## Island Perimeter

def islandPerimeter(grid):
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                count+=4
                if i-1>=0 and grid[i-1][j]==1:
                    count-=2
                if j-1>=0 and grid[i][j-1]==1:
                    count-=2
    return count

if __name__=='__main__':
    grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(islandPerimeter(grid))