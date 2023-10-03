## 36. Valid Sudoku

## Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
## Each row must contain the digits 1-9 without repetition.
## Each column must contain the digits 1-9 without repetition.
## Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

def isValidSudoku(board):
    h=[[] for _ in range(9)]
    v=[[] for _ in range(9)]
    s=[[] for _ in range(9)]
    print(h[0])
    for i in range(9):
        for j in range(9):
            if board[i][j]=='.':
                continue
            if board[i][j] in h[i] or board[i][j] in v[j]:
                return False
            else:
                h[i].append(board[i][j])
                v[j].append(board[i][j])
            if board[i][j] in s[i//3*3+j//3]:
                return False
            else:
                s[i//3*3+j//3].append(board[i][j])
    return True

if __name__=='__main__':
    board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))
        