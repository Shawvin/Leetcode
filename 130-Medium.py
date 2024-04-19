## 130. Surrounded Regions

## Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
## A region is captured by flipping all 'O's into 'X's in that surrounded region.

def solve(board):
    def dfs(i, j, board, b, e):
        if i > 0 and board[i - 1][j] == b:
            board[i - 1][j] = e
            dfs(i - 1, j, board, b, e)
        if j > 0 and board[i][j - 1] == b:
            board[i][j - 1] = e
            dfs(i, j - 1, board, b, e)
        if i < len(board) - 1 and board[i + 1][j] == b:
            board[i + 1][j] = e
            dfs(i + 1, j, board, b, e)
        if j < len(board[0]) - 1 and board[i][j + 1] == b:
            board[i][j + 1] = e
            dfs(i, j + 1, board, b, e)
    for i in range(len(board[0])):
        if board[0][i]=='O':
            board[0][i]='1'
            dfs(0,i,board,'O','1')
        if board[len(board)-1][i]=='O':
            board[len(board)-1][i]='1'
            dfs(len(board)-1,i,board,'O','1')
    for j in range(len(board)):
        if board[j][0]=='O':
            board[j][0]='1'
            dfs(j,0,board,'O','1')
        if board[j][len(board[0])-1]=='O':
            board[j][len(board[0])-1]='1'
            dfs(j,len(board[0])-1,board,'O','1')
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='O':
                board[i][j]='X'
                dfs(i, j, board, 'O','X')
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='1':
                board[i][j]='O'
    return board

if __name__=='__main__':
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print(solve(board))