## 1277. Count Square Submatrices with All Ones

class Solution:
    def countSquares(self, matrix) -> int:
        m=len(matrix)
        n=len(matrix[0])
        res=0
        for i in range(m):
            for j in range(n):
                if i==0:
                    res+=matrix[i][j]
                    continue
                if j==0:
                    res+=matrix[i][j]
                elif matrix[i][j]==1:
                    if matrix[i-1][j-1]>0:
                        matrix[i][j]=min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])+1
                    res+=matrix[i][j]
        return res
    
    def countSquares2(self, matrix) -> int:
        m=len(matrix)
        n=len(matrix[0])
        res=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1 and i>0 and j>0 and matrix[i-1][j-1]>0:
                    matrix[i][j]=min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])+1
                res+=matrix[i][j]
        return res
    

if __name__=='__main__':
    matrix =[
      [0,1,1,1],
      [1,1,1,1],
      [0,1,1,1]
    ]
    print(Solution().countSquares(matrix))