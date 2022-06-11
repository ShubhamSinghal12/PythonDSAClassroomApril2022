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
                if not board[i][j] and isItPossible(board,i,j):
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
        if isItPossible(board,row,col):
            board[row][col] = True
            qc(board,tq,qpsf+1,ans+"b"+str(row)+str(col)+" ",row,col+1)
            board[row][col] = False

        qc(board,tq,qpsf,ans,row,col+1)
def isItPossible(board,row,col):

    #Row 
    r = row
    c = col
    while c >= 0:
        if board[r][c] :
            return False
        c -= 1
    
    #Column
    r = row
    c = col
    while r >= 0:
        if board[r][c] :
            return False
        r -= 1

    #Left Diagonal
    r = row
    c = col
    while c >= 0 and r >= 0:
        if board[r][c] :
            return False
        c -= 1
        r -= 1
    
    #Right Diagonal
    r = row
    c = col
    while c < len(board[0]) and r >= 0:
        if board[r][c] :
            return False
        c += 1
        r -= 1
    
    return True


def nqueens(board,tq,qpsf,ans):
    if tq == qpsf:
        print(ans)
    else:
        for c in range(len(board[0])):
            if not board[qpsf][c] and isItPossible(board,qpsf,c):
                board[qpsf][c] = True
                nqueens(board,tq,qpsf+1,ans+"qb{}{} ".format(qpsf,c))
                board[qpsf][c] = False

m = 4
n = 4
tq = 4
board = [[False for i in range(n)]for j in range(m)]

nqueens(board,tq,0,"")
# qc(board,tq,0,"",0,0)
# queensComb(board,tq,0,"",0,0)