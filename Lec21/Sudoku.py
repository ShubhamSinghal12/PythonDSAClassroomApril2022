grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

def sudoku(grid,row,col):
    if row == len(grid):
        for i in grid:
            print(i)
        print()
    elif col == len(grid[0]):
        sudoku(grid,row+1,0)
    elif grid[row][col] != 0:
        sudoku(grid,row,col+1)
    else:
        for i in range(1,10):
            if isItPossible(grid,row,col,i):
                grid[row][col] = i
                sudoku(grid,row,col+1)
                grid[row][col] = 0

def isItPossible(grid,row,col,val):
    for i in range(len(grid[0])):
        if grid[row][i] == val:
            return False
    for i in range(len(grid)):
        if grid[i][col] == val:
            return False
    
    # r = row-row%3
    # c = col-col%3
    r = (row//3)*3
    c = (col//3)*3

    for i in range(r,r+3):
        for j in range(c,c+3):
            if grid[i][j] == val:
                return False
    
    return True


sudoku(grid,0,0)

