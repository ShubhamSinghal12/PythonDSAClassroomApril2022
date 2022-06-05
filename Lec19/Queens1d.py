
n = 4
tq = 2
board = [False for i in range(n)]

def queensPerm(board,tq,qpsf,ans):
    if qpsf == tq:
        print(ans)
    else:
        for i in range(len(board)):
            if not board[i]:
                board[i] = True
                queensPerm(board,tq,qpsf+1,ans+"q{}b{} ".format(qpsf,i))
                board[i] = False


def queensComb(board,tq,qpsf,ans,lp):
    if qpsf == tq:
        print(ans)
    else:
        for i in range(lp+1,len(board)):
            if not board[i]:
                board[i] = True
                queensComb(board,tq,qpsf+1,ans+"qb{} ".format(i),i)
                board[i] = False

def qc(board,tq,qpsf,ans,i):
    if qpsf == tq:
        print(ans)
    elif i >= len(board):
        return 
    else:
        board[i] = True
        qc(board,tq,qpsf+1,ans+"b"+str(i),i+1)
        board[i] = False

        qc(board,tq,qpsf,ans,i+1)

qc(board,tq,0,"",0)
# queensComb(board,tq,0,"",-1)
# queensPerm(board,tq,0,"")

