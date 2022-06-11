m = 2
n = 3
tq = 2
board = [[False for i in range(n)]for j in range(m)]


def queensPerm(board,tq,qpsf,ans):
    if qpsf == tq:
        print(ans)
    else:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if not board[i][j]:
                    board[i][j] = True
                    queensPerm(board,tq,qpsf+1,ans+"q{}b{}{} ".format(qpsf,i,j))
                    board[i][j] = False


def queensComb(board,tq,qpsf,ans,row,col):
    if qpsf == tq:
        print(ans)
    else:
        for i in range(row,len(board)):
            if i == row:
                c = col
            else:
                c = 0
            for j in range(c,len(board[i])):
                if not board[i][j]:
                    board[i][j] = True
                    queensComb(board,tq,qpsf+1,ans+"qb{}{} ".format(i,j),i,j)
                    board[i][j] = False

def qc(board,tq,qpsf,ans,row,col):
    if qpsf == tq:
        print(ans)
    elif row >= len(board):
        return 
    elif col >= len(board[0]):
        qc(board,tq,qpsf,ans,row+1,0)
    else:
        board[row][col] = True
        qc(board,tq,qpsf+1,ans+"b"+str(row)+str(col)+" ",row,col+1)
        board[row][col] = False

        qc(board,tq,qpsf,ans,row,col+1)

qc(board,tq,0,"",0,0)
# queensComb(board,tq,0,"",0,0)
# queensPerm(board,tq,0,"")
