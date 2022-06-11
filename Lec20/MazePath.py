m = 3
n = 3
maze = [[0 for i in range(n)] for j in range(m)]

maze[1][1] = 2
# maze[2][0] = 2
def dispMaze(maze):
    for i in maze:
        for j in i:
            if j == 2:
                print(0,end = " ")
            else:
                print(j,end=" ")
        print()

def mazeP(maze,cr,cc,ans):
    if cr == len(maze)-1 and cc == len(maze[0])-1:
        print(ans)
        maze[cr][cc] = 1
        dispMaze(maze)
        maze[cr][cc] = 0
        return True
    elif cr >= len(maze) or cc >= len(maze[0]) or cr < 0 or cc < 0 or maze[cr][cc] != 0:
        return False
    else:
        maze[cr][cc] = 1
        row = [1,0,-1,0]
        col = [0,1,0,-1]
        st = ["D","R","U","L"]
        for i in range(len(row)):
            if mazeP(maze,cr+row[i],cc+col[i],ans+st[i]):
                maze[cr][cc] = 0
                return True
        # mazeP(maze,cr+1,cc,ans+"D")
        # mazeP(maze,cr,cc+1,ans+"R")
        # mazeP(maze,cr-1,cc,ans+"U")
        # mazeP(maze,cr,cc-1,ans+"L")
        maze[cr][cc] = 0

mazeP(maze,0,0,"")