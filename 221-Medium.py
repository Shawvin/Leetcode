## 221. Maximal Square

## Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

def maximalSquare(matrix):
    mem=[[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
    l=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='1':
                mem[i+1][j+1]=min(mem[i][j+1],mem[i+1][j],mem[i][j])+1
                l=max(l, mem[i+1][j+1])
    return l**2

if __name__=='__main__':
    matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(maximalSquare(matrix))