## 498. Diagonal Traverse

class Solution:
    def findDiagonalOrder(self, mat):
        m=len(mat)
        n=len(mat[0])
        res=[]
        reverse=True
        startRow=0
        starCol=0
        while True:
            if startRow>=m and starCol>=n:
                break
            temp=[]
            curRow=startRow
            curCol=starCol
            reverse=False if reverse else True
            while curCol<n:
                if curRow<m and curRow>=0:
                    temp.append(mat[curRow][curCol])
                curRow-=1
                curCol+=1
            if reverse:
                res=res+temp[::-1]
            else:
                res=res+temp
            if startRow<m:
                startRow+=1
            else:
                starCol+=1
        return res
    
if __name__=='__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().findDiagonalOrder(mat))
